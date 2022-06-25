<template>
  <div>
    <div>
      <v-btn @click='$router.go(-1)' elevation="4">Back</v-btn>&nbsp;&nbsp;
      <v-btn @click='$router.push("/deputy")' elevation="4">Home</v-btn>&nbsp;&nbsp;
      <v-btn @click='$router.push("/student/create")' elevation="4">Create student</v-btn>
    </div>
    <p></p>
    <h2>Students</h2>
    <div>
      <v-container fluid>
        <v-row no-gutters>
          <v-col md="2">
            <p><b>Filter student's last name</b></p>
            <v-form
            @submit.prevent="apply">
              <v-text-field
                label="Enter last name"
                solo
                v-model="studentFilterForm.lastName"
              />
            </v-form>
          </v-col>
          <v-col md="1"></v-col>
          <v-col md="2">
            <p><b>Filter student's first name</b></p>
            <v-form
            @submit.prevent="apply">
              <v-text-field
                label="Enter first name"
                solo
                v-model="studentFilterForm.firstName"
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
                v-model="studentFilterForm.groupName"
              />
            </v-form>
          </v-col>
          <v-col md="1"></v-col>
          <v-col md="2">
            <p><b>Sort by</b></p>
            <v-form
            @submit.prevent="apply">
              <v-select
                label="Choose sorting option"
                :items="sortOptions"
                filled
                v-model="studentSortForm.sortType"
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
            <p v-if="studentFilterForm.groupName !== '' || studentFilterForm.firstName !== '' || studentFilterForm.lastName !== '' || studentSortForm.sortType !== ''">
              <v-btn color="error" @click='reset'>Reset</v-btn>
            </p>
          </v-col>
          </v-row>
      </v-container>
    </div>
    <v-simple-table>
      <v-data-table-header>Students</v-data-table-header>
      <tr>
        <td><strong>Last name</strong></td>
        <td><strong>First name</strong></td>
        <td><strong>Group</strong></td>
        <td></td>
        <td></td>
      </tr>
      <tr v-for="st in students" :key="st.id">
        <td>{{ st.last_name }}</td>
        <td>{{ st.first_name }}</td>
        <td><i v-for="sub in st.group" :key="sub.id">{{ sub.name }} </i></td>
        <td><v-btn small @click='$router.push(`/student/${ st.id }`)'>Edit</v-btn></td>
        <td><v-btn small color="error" @click="deleteElem(st.id)" style="margin-right: 20px">delete</v-btn></td>
      </tr>
    </v-simple-table>
    <div>
      <v-container>
        <v-row>
          <v-col
            md="2">
          <div v-if="prevPage != null" class="prevPageButton">
        <v-btn color="primary" @click='prevPageLoad'>Previous page</v-btn>&nbsp;&nbsp;
      </div>
          </v-col>
          <v-col md="1"></v-col>
          <v-col
            md="2">
      <div v-if="nextPage != null" class="prevPageButton">
        <v-btn color="primary" @click='nextPageLoad'>Next page</v-btn>
      </div>
          </v-col>
          </v-row>
      </v-container>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Student',
  data: () => ({
    students: [],
    prevPage: '',
    nextPage: '',
    studentFilterForm: {
      firstName: '',
      lastName: '',
      groupName: ''
    },
    studentSortForm: {
      sortType: ''
    },
    orderBy: '',
    mapper: { 'First Name - Ascending': 'first_name', 'First Name - Descending': '-first_name', 'Last Name - Ascending': 'last_name', 'Last Name - Descending': '-last_name', 'Group Name - Ascending': 'group__name', 'Group Name - Descending': '-group__name' },
    sortOptions: ['First Name - Ascending', 'First Name - Descending', 'Last Name - Ascending', 'Last Name - Descending', 'Group Name - Ascending', 'Group Name - Descending']
    // sortOptions: Object.keys(this.mapper)
  }),
  created () {
    this.axios
      .get('http://127.0.0.1:8000/student/list/')
      .then((res) => {
        this.students = res.data.results
        this.prevPage = res.data.previous
        this.nextPage = res.data.next
      })
      .catch((error) => {
        console.log(error)
      })
  },
  methods: {
    async apply () {
      this.orderBy = this.mapper[this.studentSortForm.sortType]
      await this.axios
        .get('http://127.0.0.1:8000/student/list/' + '?first_name=' + this.studentFilterForm.firstName + '&last_name=' + this.studentFilterForm.lastName + '&group__name=' + this.studentFilterForm.groupName + '&ordering=' + this.orderBy)
        .then((res) => {
          this.students = res.data.results
          this.nextPage = res.data.next
          this.prevPage = res.data.previous
        })
    },
    async reset () {
      await this.axios
        .get('http://127.0.0.1:8000/student/list/')
        .then((res) => {
          this.students = res.data.results
          this.nextPage = res.data.next
          this.prevPage = res.data.previous
          this.studentFilterForm.groupName = ''
          this.studentFilterForm.firstName = ''
          this.studentFilterForm.lastName = ''
          this.studentSortForm.sortType = ''
          this.orderBy = ''
        })
    },
    async prevPageLoad () {
      await this.axios
        .get(this.prevPage)
        .then((res) => {
          this.students = res.data.results
          this.nextPage = res.data.next
          this.prevPage = res.data.previous
        })
    },
    async nextPageLoad () {
      await this.axios
        .get(this.nextPage)
        .then((res) => {
          this.students = res.data.results
          this.nextPage = res.data.next
          this.prevPage = res.data.previous
        })
    },
    async deleteElem (st) {
      await this.axios
        .delete(`http://127.0.0.1:8000/student/${st}`)
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
