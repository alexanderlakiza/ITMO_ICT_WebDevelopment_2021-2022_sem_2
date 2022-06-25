<template>
  <div>
    <div>
      <v-btn @click='$router.go(-1)' elevation="4">Back</v-btn>&nbsp;&nbsp;
      <v-btn @click='$router.push("/deputy")' elevation="4">Home</v-btn>&nbsp;&nbsp;
      <v-btn @click='$router.push("/group/create")' elevation="4">Create group</v-btn>
    </div>
    <p></p>
    <h2>Groups</h2>
    <div>
      <v-container fluid>
        <v-row no-gutters>
          <v-col
          md="3">
            <p><b>Search groups by name</b></p>
            <v-form
            @submit.prevent="apply"
          >
              <v-text-field
                label="Enter group's name"
                solo
                v-model="GroupsSearchForm.groupName"
              />
            </v-form>
          </v-col>
          <v-col
            md="1">
          </v-col>
          <v-col
            md="3">
            <p><b>Sort groups by name</b></p>
            <v-form
            @submit.prevent="apply"
          >
              <v-select
                label="Choose sorting type"
                filled
                :items="sortOptions"
                v-model="GroupsSortForm.sortType"
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
            <p v-if="GroupsSearchForm.groupName !== '' || GroupsSortForm.sortType !== ''">
              <v-btn color="error" @click='reset'>Reset</v-btn>
              </p>
          </v-col>
        </v-row>
      </v-container>
    </div>
    <v-simple-table>
      <v-data-table-header>Groups</v-data-table-header>
      <tr>
        <td><strong>Group Name</strong></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
      </tr>
      <tr v-for="el in groups" :key="el.id">
        <td>{{ el.name }}</td>
        <td>
          <v-btn small @click='$router.push(`/grouplist/${ el.id }`)' color="primary">Group List</v-btn>
        </td>
        <td>
          <v-btn small @click='$router.push(`/schedule/${ el.id }`)' color="accent">Group Schedule</v-btn>
        </td>
        <td>
          <v-btn small @click='$router.push(`/group/${ el.id }`)'>Edit</v-btn>
        </td>
        <td>
          <v-btn small color="error" @click="deleteElem(el.id)" style="margin-right: 20px">delete</v-btn>
        </td>
      </tr>
    </v-simple-table>
    <div>
      <div v-if="prevPage != null" class="prevPageButton">
        <v-btn color="primary" @click='prevPageLoad'>Previous page</v-btn>&nbsp;&nbsp;
      </div>
      <div v-if="nextPage != null" class="prevPageButton">
        <v-btn color="primary" @click='nextPageLoad'>Next page</v-btn>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data: () => ({
    GroupsSearchForm: {
      groupName: ''
    },
    GroupsSortForm: {
      sortType: ''
    },
    groups: [],
    nextPage: '',
    prevPage: '',
    sortOptions: ['Name Ascending', 'Name Descending'],
    orderBy: ''
  }),
  name: 'GroupCreate',
  // data: () => ({
  //   groups: []
  // }),
  created () {
    this.axios
      .get('http://127.0.0.1:8000/group/list/')
      .then((res) => {
        this.groups = res.data.results
        this.nextPage = res.data.next
        this.prevPage = res.data.previous
      })
      .catch((error) => {
        console.log(error)
      })
  },
  methods: {
    async reset () {
      await this.axios
        .get('http://127.0.0.1:8000/group/list/')
        .then((res) => {
          this.groups = res.data.results
          this.nextPage = res.data.next
          this.prevPage = res.data.previous
          this.GroupsSearchForm.groupName = ''
          this.GroupsSortForm.sortType = ''
          this.orderBy = ''
        })
    },
    async apply () {
      if (this.GroupsSortForm.sortType === 'Name Ascending') {
        this.orderBy = 'name'
      } else if (this.GroupsSortForm.sortType === 'Name Descending') {
        this.orderBy = '-name'
      }
      await this.axios
        .get('http://127.0.0.1:8000/group/list/' + '?search=' + this.GroupsSearchForm.groupName + '&ordering=' + this.orderBy)
        .then((res) => {
          this.groups = res.data.results
          this.nextPage = res.data.next
          this.prevPage = res.data.previous
        })
        .catch((error) => {
          console.log(error)
          alert('Invalid group name')
        })
    },
    async prevPageLoad () {
      await this.axios
        .get(this.prevPage)
        .then((res) => {
          this.groups = res.data.results
          this.nextPage = res.data.next
          this.prevPage = res.data.previous
        })
    },
    async nextPageLoad () {
      await this.axios
        .get(this.nextPage)
        .then((res) => {
          this.groups = res.data.results
          this.nextPage = res.data.next
          this.prevPage = res.data.previous
        })
    },
    async deleteElem (elem) {
      await this.axios
        .delete(`http://127.0.0.1:8000/group/${elem}`)
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
  text-align: center;
  padding: 0.5rem;
}
</style>
