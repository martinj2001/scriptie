<template>
    <div id='filterContainer'>
        <div class='organizationSelect'>
            <h4>Filter organizations</h4>
            <multiselect class='select' v-model="valueOrganizations" :options="optionsOrganizations" :multiple="true" placeholder="Type to search" track-by="name"
            label="name">
            <span slot="noResult">Oops! No elements found. Consider changing the search query.</span>\
            </multiselect>
        </div>
        <div class='fieldSelect'>
            <h4>Filter fields</h4>
            <multiselect class='select' v-model="valueFields" :options="optionsFields" :multiple="true" placeholder="Type to search" track-by="name"
            label="name">
            <span slot="noResult">Oops! No elements found. Consider changing the search query.</span>\
            </multiselect>
        </div>
        
    </div>
</template>
  
<script>
import Multiselect from 'vue-multiselect'
export default {
    name: 'FilterContainer',
    components: {
        Multiselect
    },
    data() {
        return {
            organizations: [],
            fields: [],
            valueOrganizations: [],
            optionsOrganizations: [],
            valueFields: [],
            optionsFields: [],
        }
    },
    beforeMount() {
        this.getOrganizations();
        this.getFields();        
    },
    methods: {
        getOrganizations() {
            try {
                this.$http.get(process.env.VUE_APP_API_URL + '/organizations').then(response => {
                    this.organizations = response.data;                    
                    console.log(JSON.parse(JSON.stringify(response.data)));
                    this.fillFilters(this.organizations, this.optionsOrganizations);
                });
            } catch (error) {
                console.log(error);
            }
        },
        getFields() {
            try {
                this.$http.get(process.env.VUE_APP_API_URL + '/fields').then(response => {
                    this.fields = response.data;                    
                    console.log(JSON.parse(JSON.stringify(response.data)));
                    this.fillFilters(this.fields, this.optionsFields);
                });
            } catch (error) {
                console.log(error);
            }
        },
        fillFilters(arr, options) {            
            arr.forEach((val, index) => {                
                options.push({name: val, code: val})                
            })
        }
    },
    watch: {
        valueOrganizations: function(val) {
            let organizations = val.map(a => a.name);
            this.$emit('organizationsFilter', organizations);
        },
        valueFields: function(val) {
            let fields = val.map(a => a.name);
            this.$emit('fieldsFilter', fields);
        }
    }
}
</script>

<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>
<style>
.organizationSelect, .fieldSelect {
    display: inline-block;
    width: 49%;
}
</style>
