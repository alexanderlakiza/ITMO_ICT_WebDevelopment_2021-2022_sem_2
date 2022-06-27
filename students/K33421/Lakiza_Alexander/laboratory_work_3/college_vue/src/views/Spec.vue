<template>
  <div>
    <div>
      <v-btn @click='$router.go(-1)' elevation="4">Back</v-btn>&nbsp;&nbsp;
      <v-btn @click='$router.push("/deputy")' elevation="4">Home</v-btn>&nbsp;&nbsp;
      <v-btn @click='$router.push("/spec/create")' elevation="4">Create specilaty</v-btn>
    </div>
    <p></p>
    <h2>Specialties</h2>
      <v-container fluid>
        <v-row no-gutters>
          <v-col md="3">
            <p><b>Filter by specialty name</b></p>
            <v-form
            @submit.prevent="apply">
              <v-text-field
                label="Enter spec name"
                solo
                v-model="specFilterForm.specName"
              />
            </v-form>
          </v-col>
          <v-col md="1"></v-col>
          <v-col md="2">
            <p><b>Filter by group name</b></p>
            <v-form
            @submit.prevent="apply">
              <v-text-field
                label="Enter group name"
                solo
                v-model="specFilterForm.groupName"
              />
            </v-form>
          </v-col>
          <v-col md="1"></v-col>
          <v-col md="2">
            <p><b>IT specialty ???</b></p>
            <v-form
            @submit.prevent="apply">
              <v-checkbox
                v-model="specFilterForm.itSpec"
                color="primary"
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
            <p v-if="specFilterForm.groupName !== '' || specFilterForm.specName !== '' || specFilterForm.itSpec !== '' || sortForm.sortType !== ''">
              <v-btn color="error" @click='reset'>Reset</v-btn>
            </p>
          </v-col>
        </v-row>
      </v-container>
    <v-simple-table>
      <v-data-table-header>Students</v-data-table-header>
      <tr>
        <td><strong>Specialty name</strong></td>
        <td><strong>Groups</strong></td>
        <td></td>
        <td></td>
      </tr>
      <tr v-for="st in specs" :key="st.id">
        <td>{{ st.name }}</td>
        <td><i v-for="sub in st.groups" :key="sub.id">{{ sub.name }} </i></td>
        <td><v-btn small @click='$router.push(`/spec/${ st.id }`)'>Edit</v-btn></td>
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
  name: 'Spec',
  data: () => ({
    specs: [],
    prevPage: '',
    nextPage: '',
    specFilterForm: {
      specName: '',
      groupName: '',
      itSpec: ''
    },
    sortForm: {
      sortType: ''
    },
    orderBy: '',
    mapper: { 'Spec Name - Asc': 'name', 'Spec Name - Desc': '-name', 'Group Name': 'groups__name', 'Group Name - Desc': '-groups__name' },
    sortOptions: ['Spec Name - Asc', 'Spec Name - False', 'Group Name - Asc', 'Group Name - Desc']
  }),
  created () {
    this.axios
      .get('http://127.0.0.1:8000/spec/list/')
      .then((res) => {
        this.specs = res.data.results
        this.prevPage = res.data.previous
        this.nextPage = res.data.next
      })
      .catch((error) => {
        console.log(error)
      })
  },
  methods: {
    async apply () {
      this.orderBy = this.mapper[this.sortForm.sortType]
      await this.axios
        .get('http://127.0.0.1:8000/spec/list/' + '?name=' + this.specFilterForm.specName + '&groups__name=' + this.specFilterForm.groupName + '&it_specialty=' + this.specFilterForm.itSpec + '&ordering=' + this.orderBy)
        .then((res) => {
          this.specs = res.data.results
          this.nextPage = res.data.next
          this.prevPage = res.data.previous
        })
    },
    async reset () {
      await this.axios
        .get('http://127.0.0.1:8000/spec/list/')
        .then((res) => {
          this.specs = res.data.results
          this.nextPage = res.data.next
          this.prevPage = res.data.previous
          this.specFilterForm.groupName = ''
          this.specFilterForm.specName = ''
          this.specFilterForm.itSpec = ''
          this.sortForm.sortType = ''
          this.orderBy = ''
        })
    },
    async prevPageLoad () {
      await this.axios
        .get(this.prevPage)
        .then((res) => {
          this.specs = res.data.results
          this.nextPage = res.data.next
          this.prevPage = res.data.previous
        })
    },
    async nextPageLoad () {
      await this.axios
        .get(this.nextPage)
        .then((res) => {
          this.specs = res.data.results
          this.nextPage = res.data.next
          this.prevPage = res.data.previous
        })
    },
    async deleteElem (st) {
      await this.axios
        .delete(`http://127.0.0.1:8000/spec/${st}`)
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

<style scoped>

</style>
