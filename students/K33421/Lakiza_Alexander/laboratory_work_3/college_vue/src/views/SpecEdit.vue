<template>
  <div class="add">
    <div>
      <v-btn @click='$router.go(-1)' elevation="4">Back</v-btn>&nbsp;&nbsp;
      <v-btn @click='$router.push("/deputy")' elevation="4">Home</v-btn>
    </div>
    <v-form
      @submit.prevent="update"
      ref="addForm"
      class="my-2"
    >
      <v-row>
        <v-col cols="4" class="mx-auto">
          <v-text-field
            label="Enter specialty name"
            v-model="addForm.name"
          />
          <v-checkbox
            label="Is it IT specialty???"
            v-model="addForm.it_specialty"
          />
          <v-select
            label="Choose group"
            v-model="addSub.groups"
            multiple="multiple"
            :items="subjects"
            item-text="label"
            item-value="code"
            :reduce="option => option.code">
            <option v-for="sub in subjects" :key="sub.id">
              {{ sub.label }}
            </option>
          </v-select>
          <v-btn color="primary" @click="update">update</v-btn>
        </v-col>
      </v-row>
    </v-form>
  </div>
</template>

<script>
export default {
  name: 'SpecEdit',
  data: () => ({
    t_id: 0,
    t_cur: {
      name: '',
      it_specialty: false,
      groups: []
    },
    subjects: [],
    addForm: {
      name: '',
      it_specialty: ''
    },
    addSub: {
      groups: []
    }
  }),
  created () {
    this.t_id = this.$route.params.spec_id
    this.axios
      .get(`http://127.0.0.1:8000/spec/${this.t_id}`)
      .then((res) => {
        console.log(res.data)
        this.t_cur = res.data
        this.addForm.name = this.t_cur.name
        this.addForm.it_specialty = this.t_cur.it_specialty
      })
    this.axios
      .get('http://127.0.0.1:8000/groupspec/list/')
      .then((res) => {
        for (const i of res.data) {
          if (i.specialty.toString() === this.t_id) {
            this.t_cur.groups.push(i.group)
            this.addSub.groups.push(i.group)
          }
        }
        console.log(res.data)
      })
    this.axios
      .get('http://127.0.0.1:8000/all_groups/')
      .then((res) => {
        const data = res.data
        console.log(res.data)
        for (let i = 0; i < res.data.length; i++) {
          const label = `${data[i].name}`
          const id = data[i].id
          this.subjects.push({ label: label, code: id })
        }
      })
      .catch((error) => {
        console.log(error)
      })
  },
  methods: {
    async update () {
      await this.axios
        .put(`http://127.0.0.1:8000/spec/${this.t_id}/`, this.addForm)
        .then((res) => {
          console.log(res)
        })
        .catch((error) => {
          console.log(error)
        })
      console.log(this.t_cur)
      for (const sub of this.t_cur.groups) {
        console.log(sub)
        const id = await this.axios
          .get('http://127.0.0.1:8000/groupspec/list/')
          .then((res) => {
            console.log(res.data)
            return res.data.filter(val => val.specialty.toString() === this.t_id && val.group === sub.id)[0].id
          })
          .catch((error) => {
            console.log(error)
          })
        await this.axios
          .delete(`http://127.0.0.1:8000/groupspec/${id}/`)
          .then((res) => {
            console.log(res)
          })
          .catch((error) => {
            console.log(error)
          })
      }
      for (const sub of this.addSub.groups) {
        await this.axios
          .post('http://127.0.0.1:8000/groupspec/create/', {
            specialty: this.t_id,
            group: sub
          })
          .then((res) => {
            console.log(res)
          })
          .catch((error) => {
            console.log(error)
          })
      }
      await this.$router.push('/spec')
    }
  }
}
</script>
