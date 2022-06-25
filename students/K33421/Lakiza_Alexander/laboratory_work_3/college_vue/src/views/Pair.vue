<template>
  <div>
    <div>
      <v-btn @click='$router.go(-1)' elevation="4">Back</v-btn>&nbsp;&nbsp;
      <v-btn @click='$router.push("/deputy")' elevation="4">Home</v-btn>&nbsp;&nbsp;
      <v-btn @click='$router.push("/pair/create")' elevation="4">Create pair</v-btn>
    </div>
    <p></p>
    <h2>Pairs</h2>
    <v-container fluid>
      <v-row no-gutters>
        <v-col md="2">
          <p><b>Filter by subject</b></p>
          <v-form
            @submit.prevent="apply">
            <v-text-field
              label="Enter subject"
              solo
              v-model="pairForm.subject"
            />
          </v-form>
        </v-col>
        <v-col md="1"></v-col>
        <v-col md="2">
          <p><b>Filter by group</b></p>
          <v-form
            @submit.prevent="apply">
            <v-text-field
              label="Enter group"
              solo
              v-model="pairForm.group"
            />
          </v-form>
        </v-col>
        <v-col md="1"></v-col>
        <v-col md="2">
          <p><b>Filter by day of week</b></p>
          <v-form
            @submit.prevent="apply">
            <v-select
              label="Enter week day"
              solo
              :items="days"
              v-model="pairForm.dayOfWeek"
            />
          </v-form>
        </v-col>
        <v-col md="1"></v-col>
        <v-col md="2">
          <p><b>Filter by teacher</b></p>
          <v-form
            @submit.prevent="apply">
            <v-text-field
              label="Enter teacher last name"
              solo
              v-model="pairForm.teacher"
            />
          </v-form>
        </v-col>
      </v-row>
      <v-row no-gutters>
        <v-col md="2">
          <p><b><i>Enter min room number</i></b></p>
          <v-form
            @submit.prevent="apply">
            <v-text-field
              label="Enter min room number"
              v-model="roomForm.roomMin"
            />
          </v-form>
        </v-col>
        <v-col md="1"></v-col>
        <v-col md="2">
          <p><b><i>Enter max room number</i></b></p>
          <v-form
            @submit.prevent="apply">
            <v-text-field
              label="Enter max room number"
              v-model="roomForm.roomMax"
            />
          </v-form>
        </v-col>
        <v-col md="1"></v-col>
        <v-col md="2">
          <p><b><i>Enter min lesson number</i></b></p>
          <v-form
            @submit.prevent="apply">
            <v-select
              :items="lessonN"
              label="Enter min lesson number"
              v-model="lessonForm.lessonMin"
            />
          </v-form>
        </v-col>
        <v-col md="1"></v-col>
        <v-col md="2">
          <p><b><i>Enter max lesson number</i></b></p>
          <v-form
            @submit.prevent="apply">
            <v-select
              :items="lessonN"
              label="Enter max lesson number"
              v-model="lessonForm.lessonMax"
            />
          </v-form>
        </v-col>
      </v-row>
      <v-row no-gutters>
        <v-col md="2">
          <p><b>Filter by room</b></p>
          <v-form
            @submit.prevent="apply">
            <v-text-field
              label="Enter room number"
              solo
              v-model="pairForm.room"
            />
          </v-form>
        </v-col>
        <v-col md="1"></v-col>
        <v-col md="2">
          <p><b>Filter by number of lesson</b></p>
          <v-form
            @submit.prevent="apply">
            <v-text-field
              label="Enter number of lesson"
              solo
              v-model="pairForm.lessonNum"
            />
          </v-form>
        </v-col>
        <v-col md="2"></v-col>
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
        <v-col md="2">
          <p
            v-if="pairForm.subject !== '' || pairForm.room !== '' || pairForm.group !== '' || pairForm.dayOfWeek !== '' || pairForm.lessonNum !== '' || pairForm.teacher !== '' || lessonForm.lessonMin !== '' ||  lessonForm.lessonMax !== '' || roomForm.roomMax !== '' || roomForm.roomMin !== '' || sortForm.sortType !== ''">
            <v-btn color="error" @click='reset'>Reset</v-btn>
          </p>
        </v-col>
      </v-row>
    </v-container>
    <v-simple-table>
      <v-data-table-header>Pairs</v-data-table-header>
      <tr>
        <td><strong>Day's name</strong></td>
        <td><strong>Pair number</strong></td>
        <td><strong>Group</strong></td>
        <td><strong>Subject</strong></td>
        <td><strong>Room</strong></td>
        <td><strong>Teacher</strong></td>
        <td></td>
        <td></td>
      </tr>
      <tr v-for="el in elems" :key="el.id">
        <td>{{ el.name_day }}</td>
        <td>{{ el.pair_number }}</td>
        <td>{{ el.group.name }}</td>
        <td>{{ el.subject.name }}</td>
        <td>{{ el.room }}</td>
        <td>{{ el.teacher.last_name }}</td>
        <td>
          <v-btn small @click='$router.push(`/pair/${ el.id }`)'>Edit</v-btn>
        </td>
        <td>
          <v-btn small color="error" @click="deleteElem(el.id)" style="margin-right: 20px">delete</v-btn>
        </td>
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
  name: 'Pair',
  data: () => ({
    pairForm: {
      teacher: '',
      subject: '',
      group: '',
      lessonNum: '',
      dayOfWeek: '',
      room: ''
    },
    lessonN: [1, 2, 3, 4, 5, 6, 7],
    days: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
    roomForm: {
      roomMin: '',
      roomMax: ''
    },
    lessonForm: {
      lessonMin: '',
      lessonMax: ''
    },
    elems: [],
    nextPage: '',
    prevPage: '',
    sortForm: {
      sortType: ''
    },
    mapper: {
      'Teacher - Asc': 'teacher__last_name',
      'Teacher - Desc': '-teacher__last_name',
      'Subject - Asc': 'subject__name',
      'Subject - Desc': '-subject__name',
      'Group - Asc': 'group__name',
      'Group - Desc': '-group__name',
      'Number of lesson - Asc': 'pair_number',
      'Number of lesson - Desc': '-pair_number',
      'Room - Asc': 'room',
      'Room - Desc': '-room'
    },
    sortOptions: ['Teacher - Asc', 'Teacher - Desc', 'Subject - Asc', 'Subject - Desc', 'Group - Asc', 'Group - Desc', 'Number of lesson - Asc', 'Number of lesson - Desc', 'Room - Asc', 'Room - Desc']
  }),
  async created () {
    await this.axios
      .get('http://127.0.0.1:8000/pair/list/')
      .then((res) => {
        this.elems = res.data.results
        this.prevPage = res.data.previous
        this.nextPage = res.data.next
      })
      .catch((error) => {
        console.log(error)
      })
    // await this.axios
    //   .get('http://127.0.0.1:8000/group/list/')
    //   .then((res) => {
    //     console.log('this.groups', res.data)
    //     this.groups = res.data.results
    //   })
    //   .catch((error) => {
    //     console.log(error)
    //   })
    // await this.axios
    //   .get('http://127.0.0.1:8000/teacher/list/')
    //   .then((res) => {
    //     console.log('this.teachers', res.data)
    //     this.teachers = res.data.results
    //   })
    //   .catch((error) => {
    //     console.log(error)
    //   })
    // await this.axios
    //   .get('http://127.0.0.1:8000/subject/list')
    //   .then((res) => {
    //     console.log('this.subjects', res.data)
    //     this.subjects = res.data.results
    //   })
    //   .catch((error) => {
    //     console.log(error)
    //   })
    // console.log('this.pairs.length', this.pairs)
    // for (const i of this.pairs) {
    //   console.log('i', i)
    //   const gro = this.groups.filter(val => val.id === i.group)[0]
    //   console.log(gro)
    //   const tea = this.teachers.filter(val => val.id === i.teacher)[0]
    //   const sub = this.subjects.filter(val => val.id === i.subject)[0]
    //   this.elems.push({ id: i.id, pair_number: i.pair_number, name_day: i.name_day, room: i.room, group: gro.name, subject: sub.name, teacher: `${tea.first_name} ${tea.last_name}` })
    // }
  },
  methods: {
    async apply () {
      this.orderBy = this.mapper[this.sortForm.sortType]
      await this.axios
        .get('http://127.0.0.1:8000/pair/list/' + '?teacher__last_name=' + this.pairForm.teacher + '&group__name=' + this.pairForm.group + '&subject__name=' + this.pairForm.subject + '&room=' + this.pairForm.room + '&name_day=' + this.pairForm.dayOfWeek + '&pair_number=' + this.pairForm.lessonNum + '&room_min=' + this.roomForm.roomMin + '&room_max=' + this.roomForm.roomMax + '&n_lesson_min=' + this.lessonForm.lessonMin + '&n_lesson_max=' + this.lessonForm.lessonMax + '&ordering=' + this.orderBy)
        .then((res) => {
          this.elems = res.data.results
          this.nextPage = res.data.next
          this.prevPage = res.data.previous
        })
    },
    async reset () {
      await this.axios
        .get('http://127.0.0.1:8000/pair/list/' +
          '/list/')
        .then((res) => {
          this.elems = res.data.results
          this.nextPage = res.data.next
          this.prevPage = res.data.previous
          this.sortForm.sortType = ''
          this.lessonForm.lessonMin = ''
          this.lessonForm.lessonMax = ''
          this.roomForm.roomMin = ''
          this.roomForm.roomMax = ''
          this.orderBy = ''
          this.pairForm.teacher = ''
          this.pairForm.subject = ''
          this.pairForm.group = ''
          this.pairForm.room = ''
          this.pairForm.lessonNum = ''
          this.pairForm.dayOfWeek = ''
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
        .delete(`http://127.0.0.1:8000/pair/${elem}`)
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
