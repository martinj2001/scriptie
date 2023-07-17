
<template>
  <div>
    <h2>Home Page</h2>
    <hr>
    <div id="filtering">
      <h3>Filters</h3>
      <FilterContainer class='filterContainer' @organizationsFilter="organizationsFilterChanged" @fieldsFilter="fieldsFilterChanged"/>
    </div>
    <hr>
    <h3>Completeness</h3>
    <hr>
    <Completeness :data="data" :showOrganizations="showOrganizations" :showFields="showFields"/>
    
    <hr>
    <h3>Correctness</h3>
    <hr>
    <Correctness :data="data"/>

    <hr>
    <h3>Accessibility</h3>
    <hr>
    <Accessibility :data="data" :showOrganizations="showOrganizations" :showFields="showFields"/>
  </div>
  
  
</template>


<script>
import Accessibility from './dashboards/Accessibility/Accessibility.vue';
import Completeness from './dashboards/Completeness/Completeness.vue';
import Correctness from './dashboards/Correctness/Correctness.vue';
import FilterContainer from './filtering/FilterContainer.vue';
export default {
  name: 'HomePage',
  components: {
    Completeness,
    Correctness,
    Accessibility,
    FilterContainer
},
  data() {
    return {
      data: {},
      organizationsFilter: [],
      fieldsFilter: [],
      showOrganizations: true,
      showFields: true,
    }
  },
  mounted() {
    this.getAlgorithmsData([], []);
  },
  methods: {
    getAlgorithmsData(filterOrganizations = [], filterFields = []) {
      try {          
          if(filterOrganizations.length == 0 && filterFields.length == 0)
          {
            this.$http.get(process.env.VUE_APP_API_URL + '/algorithms/score').then(response => {
            this.data = response.data;
            console.log(typeof(this.data));
            console.log(JSON.parse(JSON.stringify(response.data)))});
          }
          else {
            console.log('Need to filter!');
            let queryString = '';
            
            filterOrganizations.forEach((val) => {
              if( queryString.length == 0)
              {
                queryString += '?filterOrganizations=' + val;
              }
              else
              {
                queryString += '&filterOrganizations=' + val;
              }              
            });

            filterFields.forEach((val) => {
              if (queryString.length == 0)
              {
                queryString += '?filterFields=' + val;
              }
              else {
                queryString += '&filterFields=' + val;
              }
            })
            
            this.$http.get(process.env.VUE_APP_API_URL + '/algorithms/score' + encodeURI(queryString)).then(response => {
            this.data = response.data;
            console.log(typeof(this.data));
            console.log(JSON.parse(JSON.stringify(response.data)))});
          }
          
        
      } catch(error) {
        console.log(error);
      }
    },
    organizationsFilterChanged(value) {
      this.organizationsFilter = value;
      this.showOrganizations = value.length == 1 ? false : true;      
      this.getAlgorithmsData(this.organizationsFilter, this.fieldsFilter);
      
    },
    fieldsFilterChanged(value) {
      this.fieldsFilter = value;
      this.showFields = value.length == 1 ? false : true;
      this.getAlgorithmsData(this.organizationsFilter, this.fieldsFilter)
      
    }
  }
}
</script>



<style scoped>
div.chart-wrapper {
  display: block;
  align-items: center;
  justify-content: center
}

* {
  color: #154273;
  
}

.filterContainer {
  margin-bottom: 40px;
}
</style>