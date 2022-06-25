<template>
  <div>
    <div>
      <v-btn @click='$router.go(-1)' elevation="4">Back</v-btn>&nbsp;&nbsp;
      <v-btn @click='$router.push("/deputy")' elevation="4">Home</v-btn>&nbsp;&nbsp;
      <v-btn @click='$router.push("/teacher/create")' elevation="4">Create teacher</v-btn>
    </div>
    <p></p>
    <h2>Teachers</h2>
    <div>
      <v-container fluid>
        <v-row no-gutters>
          <v-col md="2">
            <p><b>Filter teacher's first name</b></p>
            <v-form
            @submit.prevent="apply">
              <v-text-field
                label="Enter first name"
                solo
                v-model="teacherFilterForm.firstName"
              />
            </v-form>
          </v-col>
          <v-col md="1"></v-col>
          <v-col md="2">
            <p><b>Filter teacher's last name</b></p>
            <v-form
            @submit.prevent="apply">
              <v-text-field
                label="Enter last name"
                solo
                v-model="teacherFilterForm.lastName"
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
                v-model="teacherFilterForm.subjName"
              />
            </v-form>
          </v-col>
        </v-row>
        <v-row no-gutters>
          <v-col md="2">
            <p><b>Filter room's number</b></p>
            <v-form
            @submit.prevent="apply">
              <v-text-field
                label="Enter room number"
                solo
                v-model="teacherFilterForm.room"
              />
            </v-form>
          </v-col>
          <v-col md="1"></v-col>
          <v-col md="9">
            <v-row>
              <v-col md="4">
                <p><b><i>Enter min room number</i></b></p>
            <v-form
            @submit.prevent="apply">
              <v-text-field
                label="Enter min room number"
                v-model="roomRangeForm.roomMin"
              />
            </v-form>
              </v-col>
              <v-col md="1"></v-col>
              <v-col md="4">
                <p><b><i>Enter max room number</i></b></p>
            <v-form
            @submit.prevent="apply">
              <v-text-field
                label="Enter max room number"
                v-model="roomRangeForm.roomMax"
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
                :items="sortOptions"
                filled
                v-model="teacherSortForm.sortType"
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
            <p v-if="teacherFilterForm.subjName !== '' || teacherFilterForm.firstName !== '' || teacherFilterForm.lastName !== '' || teacherSortForm.sortType !== '' || roomRangeForm.roomMax !== '' || roomRangeForm.roomMin !== ''">
              <v-btn color="error" @click='reset'>Reset</v-btn>
            </p>
          </v-col>
          </v-row>
      </v-container>
    </div>
    <v-simple-table>
      <v-data-table-header>teachers</v-data-table-header>
      <tr>
        <td><strong>First name</strong></td>
        <td><strong>Last name</strong></td>
        <td><strong>Subjects</strong></td>
        <td><strong>Room</strong></td>
        <td></td>
        <td></td>
      </tr>
      <tr v-for="el in teachers" :key="el.id">
        <td>{{ el.first_name }}</td>
        <td>{{ el.last_name }}</td>
        <td><i v-for="sub in el.subjects" :key="sub.name">{{ sub.name }} </i></td>
        <td v-if="el.room">{{ el.room }}</td>
        <td v-else> -</td>
        <td>
          <v-btn small @click='$router.push(`/teacher/${ el.id }`)'>Edit</v-btn>
        </td>
        <td>
          <v-btn small color="error" @click="deleteElem(el.id)" style="margin-right: 20px">delete</v-btn>
        </td>
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
  name: 'TeacherCreate',
  data: () => ({
    teachers: [],
    prevPage: '',
    nextPage: '',
    teacherFilterForm: {
      firstName: '',
      lastName: '',
      room: '',
      subjName: ''
    },
    roomRangeForm: {
      roomMin: '',
      roomMax: ''
    },
    teacherSortForm: {
      sortType: ''
    },
    orderBy: '',
    mapper: { 'First Name - Asc': 'first_name', 'First Name - Desc': '-first_name', 'Last Name - Asc': 'last_name', 'Last Name - Desc': '-last_name', 'Subject Name - Asc': 'subjects__name', 'Subject Name - Desc': '-subjects__name', 'Room - Asc': 'room', 'Room - Desc': '-room' },
    sortOptions: ['First Name - Asc', 'First Name - Desc', 'Last Name - Asc', 'Last Name - Desc', 'Subject Name - Asc', 'Subject Name - Desc', 'Room - Asc', 'Room - Desc']
  }),
  created () {
    this.axios
      .get('http://127.0.0.1:8000/teacher/list/')
      .then((res) => {
        this.teachers = res.data.results
        this.prevPage = res.data.previous
        this.nextPage = res.data.next
      })
      .catch((error) => {
        console.log(error)
      })
  },
  methods: {
    async apply () {
      this.orderBy = this.mapper[this.teacherSortForm.sortType]
      await this.axios
        .get('http://127.0.0.1:8000/teacher/list/' + '?first_name=' + this.teacherFilterForm.firstName + '&last_name=' + this.teacherFilterForm.lastName + '&subjects__name=' + this.teacherFilterForm.subjName + '&room=' + this.teacherFilterForm.room + '&room_min=' + this.roomRangeForm.roomMin + '&room_max=' + this.roomRangeForm.roomMax + '&ordering=' + this.orderBy)
        .then((res) => {
          this.teachers = res.data.results
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
          this.teacherFilterForm.subjName = ''
          this.teacherFilterForm.firstName = ''
          this.teacherFilterForm.lastName = ''
          this.teacherFilterForm.room = ''
          this.teacherSortForm.sortType = ''
          this.orderBy = ''
        })
    },
    async prevPageLoad () {
      await this.axios
        .get(this.prevPage)
        .then((res) => {
          this.teachers = res.data.results
          this.nextPage = res.data.next
          this.prevPage = res.data.previous
        })
    },
    async nextPageLoad () {
      await this.axios
        .get(this.nextPage)
        .then((res) => {
          this.teachers = res.data.results
          this.nextPage = res.data.next
          this.prevPage = res.data.previous
        })
    },
    async deleteElem (elem) {
      await this.axios
        .delete(`http://127.0.0.1:8000/teacher/${elem}`)
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
