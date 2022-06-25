<template>
  <div>
    <div>
      <v-btn @click='$router.go(-1)' elevation="4">Back</v-btn>&nbsp;&nbsp;
      <v-btn @click='$router.push("/deputy")' elevation="4">Home</v-btn>&nbsp;&nbsp;
      <v-btn @click='$router.push("/subject/create")' elevation="4">Create subject</v-btn>
    </div>
    <p></p>
    <h2>Subjects</h2>
    <div>
      <v-container fluid>
        <v-row no-gutters>
          <v-col
            md="3">
            <p><b>Search subjects by name</b></p>
            <v-form
              @submit.prevent="apply">
              <v-text-field
                label="Enter subject's name"
                solo
                v-model="subjectSearchForm.subjectName"
              />
            </v-form>
          </v-col>
          <v-col
            md="1">
          </v-col>
          <v-col
          md="3">
            <p><b>Sort subjects by name</b></p>
            <v-form
            @submit.prevent="apply"
          >
              <v-select
                label="Choose sorting type"
                filled
                :items="sortOptions"
                v-model="subjectSortForm.sortType"
              />
            </v-form>
          </v-col>
        </v-row>
        <v-row>
          <v-col
            md="3">
            <p>
            <v-btn color="primary" @click='apply' elevation="4">Apply</v-btn>
            </p>
          </v-col>
          <v-col
            md="1">
          </v-col>
          <v-col
            md="3">
            <p v-if="subjectSearchForm.subjectName !== '' || subjectSortForm.sortType !== ''">
              <v-btn color="error" @click='reset'>Reset</v-btn>
              </p>
          </v-col>
        </v-row>
      </v-container>
    </div>
    <v-simple-table>
      <v-data-table-header>subjects</v-data-table-header>
      <tr>
        <td><strong>Name</strong></td>
        <td></td>
        <td></td>
      </tr>
      <tr v-for="st in subjects" :key="st.id">
        <td>{{ st.name }}</td>
        <td><v-btn small @click='$router.push(`/subject/${ st.id }`)'>Edit</v-btn></td>
        <td><v-btn small color="error" @click="deleteElem(st.id)" style="margin-right: 20px">delete</v-btn></td>
      </tr>
    </v-simple-table>
    <v-div>
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
      </v-div>
    </div>
</template>

<script>
export default {
  name: 'Subject',
  data: () => ({
    subjectSearchForm: {
      subjectName: ''
    },
    subjectSortForm: {
      sortType: ''
    },
    prevPage: '',
    nextPage: '',
    subjects: [],
    sortOptions: ['Name Ascending', 'Name Descending'],
    orderBy: ''
  }),
  created () {
    console.log('create')
    this.axios
      .get('http://127.0.0.1:8000/subject/list/')
      .then((res) => {
        this.subjects = res.data.results
        this.nextPage = res.data.next
        this.prevPage = res.data.previous
      })
      .catch((error) => {
        console.log(error)
      })
  },
  methods: {
    async apply () {
      if (this.subjectSortForm.sortType === 'Name Ascending') {
        this.orderBy = 'name'
      } else if (this.subjectSortForm.sortType === 'Name Descending') {
        this.orderBy = '-name'
      }
      await this.axios
        .get('http://127.0.0.1:8000/subject/list/' + '?search=' + this.subjectSearchForm.subjectName + '&ordering=' + this.orderBy)
        .then((res) => {
          this.subjects = res.data.results
          this.nextPage = res.data.next
          this.prevPage = res.data.previous
        })
    },
    async reset () {
      await this.axios
        .get('http://127.0.0.1:8000/subject/list/')
        .then((res) => {
          this.groups = res.data.results
          this.nextPage = res.data.next
          this.prevPage = res.data.previous
          this.subjectSearchForm.subjectName = ''
          this.subjectSortForm.sortType = ''
          this.orderBy = ''
        })
    },
    async prevPageLoad () {
      await this.axios
        .get(this.prevPage)
        .then((res) => {
          this.subjects = res.data.results
          this.nextPage = res.data.next
          this.prevPage = res.data.previous
        })
    },
    async nextPageLoad () {
      await this.axios
        .get(this.nextPage)
        .then((res) => {
          this.subjects = res.data.results
          this.nextPage = res.data.next
          this.prevPage = res.data.previous
        })
    },
    async deleteElem (st) {
      await this.axios
        .delete(`http://127.0.0.1:8000/subject/${st}`)
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
