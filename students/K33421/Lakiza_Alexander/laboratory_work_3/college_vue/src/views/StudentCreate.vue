<template>
  <div class="add">
    <div>
      <v-btn @click='$router.go(-1)' elevation="4">Back</v-btn>&nbsp;&nbsp;
      <v-btn @click='$router.push("/deputy")' elevation="4">Home</v-btn>
    </div>
    <v-form
      @submit.prevent="add"
      ref="addForm"
      class="my-2"
    >
      <v-row>
        <v-col cols="3" class="mx-auto">
          <v-text-field
            label="Enter First name"
            v-model="addForm.first_name"
          />
          <v-text-field
            label="Enter Last name"
            v-model="addForm.last_name"
          />
          <v-select
            label="Choose group"
            v-model="addSub.groups"
            multiple="multiple"
            @click="getSubj"
            :items="groups"
            item-text="label"
            item-value="code"
            :reduce="option => option.code">
            <option v-for="sub in groups" :key="sub.id">
              {{ sub.label }}
            </option>
          </v-select>
          <v-btn color="primary" @click="add">add</v-btn>
        </v-col>
      </v-row>
    </v-form>
  </div>
</template>

<script>
export default {
  name: 'StudentCreate',
  data: () => ({
    student_id: '',
    groups: [],
    addForm: {
      first_name: '',
      last_name: '',
      groups: {}
    },
    addSub: {
      student: '',
      groups: []
    }
  }),
  methods: {
    async getSubj () {
      await this.axios
        .get('http://127.0.0.1:8000/all_groups/')
        .then((res) => {
          const data = res.data
          console.log(res.data)
          for (let i = 0; i < res.data.length; i++) {
            const label = `${data[i].name}`
            const id = data[i].id
            this.groups.push({ label: label, code: id })
          }
        })
        .catch((error) => {
          console.log(error)
        })
    },
    async add () {
      await this.axios
        .post('http://127.0.0.1:8000/student/create/', this.addForm)
        .then((res) => {
          console.log(res)
        })
        .catch((error) => {
          console.log(error)
        })
      await this.axios
        .get('http://127.0.0.1:8000/all_students/')
        .then((res) => {
          this.student_id = res.data[res.data.length - 1].id
        })
        .catch((error) => {
          console.log(error)
        })
      for (const sub of this.addSub.groups) {
        await this.axios
          .post('http://127.0.0.1:8000/stugroup/create/', {
            student: this.student_id,
            group: sub
          })
          .then((res) => {
            console.log(res)
          })
          .catch((error) => {
            console.log(error)
          })
      }
      await this.$router.push('/student')
    }
  }
}
</script>
