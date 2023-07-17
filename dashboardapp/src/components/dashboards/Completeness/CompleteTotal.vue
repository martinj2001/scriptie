<template>
    <div id='completenessTotal'>
      <apexchart type="radialBar" height="350" :options="options" :series="series"></apexchart>
    </div>    
</template>
  
<script>
    export default {
    name: 'CompleteTotal',
    props: {
        data: Object
    },
    data() {
        return {            
            options: {
                colors: ['#154273'],
                chart: {
                    height: 350,
                    type: 'radialBar'
                },
                plotOptions: {
                    radialBar: {
                        hollow: {
                            size: '70%'
                        }
                    }
                },
                labels: ['Lege velden']
            },
            series: [],
        }
    },
    beforeMount() {
        
    },
    methods: {
        async setCompletenessTotal() {
            
            this.series = [this.data.completeness.emptyValuesPercentage];
        },       
    },
    watch: {
        data: function(value) {
            this.setCompletenessTotal();
        }
    }
}
</script>

<style>

</style>
