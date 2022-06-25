<template>
  <div>
    <v-btn @click='$router.go(-1)' elevation="4">Back</v-btn>&nbsp;&nbsp;
    <v-btn @click='$router.push("/deputy")' elevation="4">Home</v-btn>&nbsp;&nbsp;
    <v-btn @click='$router.push("/mark/create")' elevation="4">Create mark</v-btn>
    <p></p>
    <h2>Marks</h2>
    <v-container fluid>
      <v-row no-gutters>
        <v-col md="2">
            <p><b>Filter student's first name</b></p>
            <v-form
            @submit.prevent="apply">
              <v-text-field
                label="Enter first name"
                solo
                v-model="markForm.firstName"
              />
            </v-form>
          </v-col>
          <v-col md="1"></v-col>
          <v-col md="2">
            <p><b>Filter student's last name</b></p>
            <v-form
            @submit.prevent="apply">
              <v-text-field
                label="Enter last name"
                solo
                v-model="markForm.lastName"
              />
            </v-form>
          </v-col>
          <v-col md="1"></v-col>
          <v-col md="2">
            <p><b>Filter subject's name</b></p>
            <v-form
            @submit.prevent="apply">
              <v-text-field
                label="Enter subject name"
                solo
                v-model="markForm.subjName"
              />
            </v-form>
          </v-col>
        <v-col md="1"></v-col>
        <v-col md="2">
          <p><b>Filter group's name</b></p>
            <v-form
            @submit.prevent="apply">
              <v-text-field
                label="Enter group name"
                solo
                v-model="markForm.groupName"
              />
            </v-form>
        </v-col>
      </v-row>
      <v-row no-gutters>
        <v-col md="2">
          <p><b>Filter mark value</b></p>
            <v-form
            @submit.prevent="apply">
              <v-select
                label="Enter mark value"
                solo
                :items="markOptions"
                v-model="markForm.mark"
              />
            </v-form>
        </v-col>
        <v-col md="1"></v-col>
        <v-col md="9">
          <v-row>
              <v-col md="4">
                <p><b><i>Enter min mark value</i></b></p>
            <v-form
            @submit.prevent="apply">
              <v-text-field
                label="Enter min mark value"
                v-model="markRangeForm.markMin"
              />
            </v-form>
              </v-col>
              <v-col md="1"></v-col>
              <v-col md="4">
                <p><b><i>Enter max mark value</i></b></p>
            <v-form
            @submit.prevent="apply">
              <v-text-field
                label="Enter max mark value"
                v-model="markRangeForm.markMax"
              />
            </v-form>
              </v-col>
            </v-row>
        </v-col>
      </v-row>
      <v-row no-gutters>
        <v-col md="2">
          <p><b>Sort by</b></p>
            <v-form
            @submit.prevent="apply">
              <v-select
                label="Choose sorting option"
                filled
                :items="sortOptions"
                v-model="sortForm.sortType"
              />
            </v-form>
        </v-col>
      </v-row>
      <v-row no-gutters>
          <v-col md="2">
            <p>
            <v-btn color="primary" @click='apply' elevation="4">Apply</v-btn>
            </p>
          </v-col>
          <v-col md="1"></v-col>
          <v-col md="3">
            <p v-if="markForm.subjName !== '' || markForm.mark !== '' || markForm.groupName !== '' || markForm.firstName !== '' || markForm.lastName !== '' || sortForm.sortType !== '' || markRangeForm.markMin !== '' ||  markRangeForm.markMax !== ''">
              <v-btn color="error" @click='reset'>Reset</v-btn>
            </p>
          </v-col>
          </v-row>
    </v-container>
    <v-simple-table>
      <tr>
        <td><strong>Student</strong></td>
        <td><strong>Group</strong></td>
        <td><strong>Subject</strong></td>
        <td><strong>Mark</strong></td>
        <td></td>
        <td></td>
      </tr>
      <tr v-for="elem in elems" :key="elem.id" >
        <td>{{ elem.student.first_name + ' ' + elem.student.last_name }}</td>
        <td><i>{{ elem.student.group[0].name }}</i></td>
        <td>{{ elem.subject.name }}</td>
        <td>{{ elem.mark }}</td>
        <td><v-btn small @click='$router.push(`/mark/${ elem.id }`)'>Edit</v-btn></td>
        <td><v-btn small color="error" @click="deleteElem(elem.id)" style="margin-right: 20px">delete</v-btn></td>
      </tr>
    </v-simple-table>
    <v-container>
      <v-row>
          <v-col
            md="2">
          <div v-if="prevPage != null" class="prevPageButton">
        <v-btn color="primary" @click='prevPageLoad'>Previous page</v-btn>&nbsp;&nbsp;
      </div>
          </v-col>
          <v-col
            md="2">
      <div v-if="nextPage != null" class="prevPageButton">
        <v-btn color="primary" @click='nextPageLoad'>Next page</v-btn>
      </div>
          </v-col>
        </v-row>
    </v-container>
  </div>
</template>

<script>
export default {
  name: 'MarkCreate',
  data: () => ({
    elems: [],
    nextPage: '',
    prevPage: '',
    markForm: {
      mark: '',
      lastName: '',
      firstName: '',
      subjName: '',
      groupName: ''
    },
    markOptions: [5, 4, 3, 2],
    markRangeForm: {
      markMin: '',
      markMax: ''
    },
    sortForm: {
      sortType: ''
    },
    orderBy: '',
    mapper: { 'First Name - Asc': 'student__first_name', 'First Name - Desc': '-student__first_name', 'Last Name - Asc': 'student__last_name', 'Last Name - Desc': '-student__last_name', 'Subject Name - Asc': 'subject__name', 'Subject Name - Desc': '-subject__name', 'Mark - Asc': 'mark', 'Mark - Desc': '-mark', 'Group Name - Asc': 'student__group__name', 'Group Name - Desc': '-student__group__name' },
    sortOptions: ['First Name - Asc', 'First Name - Desc', 'Last Name - Asc', 'Last Name - Desc', 'Subject Name - Asc', 'Subject Name - Desc', 'Mark - Asc', 'Mark - Desc', 'Group Name - Asc', 'Group Name - Desc']
  }),
  async created () {
    await this.axios
      .get('http://127.0.0.1:8000/mark/list/')
      .then((res) => {
        console.log('this.marks', this.elems)
        this.elems = res.data.results
        this.prevPage = res.data.previous
        this.nextPage = res.data.next
      })
      .catch((error) => {
        console.log(error)
      })
    // await this.axios
    //   .get('http://127.0.0.1:8000/all_students/')
    //   .then((res) => {
    //     console.log('this.students', res.data)
    //     this.students = res.data
    //   })
    //   .catch((error) => {
    //     console.log(error)
    //   })
    // await this.axios
    //   .get('http://127.0.0.1:8000/all_subjects/')
    //   .then((res) => {
    //     console.log('this.subjects', res.data)
    //     this.subjects = res.data
    //   })
    //   .catch((error) => {
    //     console.log(error)
    //   })
    // for (const i of this.marks) {
    //   const st = this.students.filter(val => val.id === i.student)[0]
    //   const sub = this.subjects.filter(val => val.id === i.subject)[0]
    //   this.elems.push({ id: i.id, mark: i.mark, student: `${st.first_name} ${st.last_name}`, subject: sub.name })
    // }
  },
  methods: {
    async apply () {
      this.orderBy = this.mapper[this.sortForm.sortType]
      await this.axios
        .get('http://127.0.0.1:8000/mark/list/' + '?student__first_name=' + this.markForm.firstName + '&student__last_name=' + this.markForm.lastName + '&subject__name=' + this.markForm.subjName + '&mark=' + this.markForm.mark + '&student__group__name=' + this.markForm.groupName + '&mark_min=' + this.markRangeForm.markMin + '&mark_max=' + this.markRangeForm.markMax + '&ordering=' + this.orderBy)
        .then((res) => {
          this.elems = res.data.results
          this.nextPage = res.data.next
          this.prevPage = res.data.previous
        })
    },
    async reset () {
      await this.axios
        .get('http://127.0.0.1:8000/mark/list/')
        .then((res) => {
          this.elems = res.data.results
          this.nextPage = res.data.next
          this.prevPage = res.data.previous
          this.markForm.subjName = ''
          this.markForm.firstName = ''
          this.markForm.lastName = ''
          this.markForm.mark = ''
          this.markForm.groupName = ''
          this.markRangeForm.markMin = ''
          this.markRangeForm.markMax = ''
          this.sortForm.sortType = ''
          this.orderBy = ''
        })
    },
    async prevPageLoad () {
      await this.axios
        .get(this.prevPage)
        .then((res) => {
          this.elems = res.data.results
          this.nextPage = res.data.next
          this.prevPage = res.data.previous
        })
    },
    async nextPageLoad () {
      await this.axios
        .get(this.nextPage)
        .then((res) => {
          this.elems = res.data.results
          this.nextPage = res.data.next
          this.prevPage = res.data.previous
        })
    },
    async deleteElem (elem) {
      await this.axios
        .delete(`http://127.0.0.1:8000/mark/${elem}`)
        .then((res) => {
          console.log(res)
          this.$router.go(0)
        })
        .catch((error) => {
          console.log(error)
        })
    }
  }
}
</script>

<style>
  table {
    margin-top: 50px;
    width: 100%;
  }
  td {
    text-align: left;
    padding: 0.5rem;
  }
</style>
