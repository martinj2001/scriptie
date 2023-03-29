<template>
    <div id='completenessTotal'>
      <apexchart type="radialBar" height="350" :options="options" :series="series"></apexchart>
    </div>    
</template>
  
<script>
    export default {
    name: 'CompleteTotal',
    props: ['data'],
    data() {
        return {            
            options: {
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
        this.setCompletenessTotal();
    },
    methods: {
        async setCompletenessTotal() {
            console.log('hoi')
            console.log(this.data)
            this.series = [this.data.completeness.emptyValuesPercentage];
        },       
    }
}
</script>

<style>

</style>
