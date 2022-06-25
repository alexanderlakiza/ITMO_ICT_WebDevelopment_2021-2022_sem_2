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
          <v-select
            label="Choose student"
            v-model="addForm.student"
            :items="students"
            item-text="label"
            item-value="code"
            :reduce="option => option.code">
            <option v-for="st in students" :key="st.id">
              {{ st.label }}
            </option>
          </v-select>
          <v-select
            label="Choose subject"
            v-model="addForm.subject"
            :items="subjects"
            item-text="label"
            item-value="code"
            :reduce="option => option.code">
            <option v-for="sub in subjects" :key="sub.id">
              {{ sub.label }}
            </option>
          </v-select>
          <v-select
            label="Enter mark"
            v-model="addForm.mark"
            :items="markTypes"
          />
          <v-btn color="primary" @click="update">update</v-btn>
        </v-col>
      </v-row>
    </v-form>
  </div>
</template>

<script>
export default {
  name: 'MarkEdit',
  data: () => ({
    st_id: 0,
    st_cur: {},
    subjects: [],
    students: [],
    addForm: {
      student: '',
      subject: '',
      mark: ''
    },
    markTypes: [5, 4, 3, 2]
  }),
  created () {
    this.st_id = this.$route.params.mark_id
    this.axios
      .get(`http://127.0.0.1:8000/mark/${this.st_id}`)
      .then((res) => {
        this.st_cur = res.data
        this.addForm.student = this.st_cur.student
        this.addForm.subject = this.st_cur.subject
        this.addForm.mark = this.st_cur.mark
        console.log(this.st_cur)
      })
    this.axios
      .get('http://127.0.0.1:8000/all_students/')
      .then((res) => {
        const data = res.data
        for (let i = 0; i < res.data.length; i++) {
          console.log(data[i].group)
          const label = `${data[i].first_name} ${data[i].last_name} ${data[i].group[0].name}`
          const id = data[i].id
          this.students.push({ label: label, code: id })
        }
      })
      .catch((error) => {
        console.log(error)
      })
    this.axios
      .get('http://127.0.0.1:8000/all_subjects/')
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
        .put(`http://127.0.0.1:8000/mark/${this.st_id}/`, this.addForm)
        .then((res) => {
          console.log(res)
          this.$refs.addForm.reset()
          this.$router.push('/mark')
        })
        .catch((error) => {
          console.log(error)
        })
      await this.$router.push('/mark')
    }
  }
}
</script>
