<template>
    <div id='datecorrectness'>
      <apexchart type="radialBar" height="350" :options="options" :series="series"></apexchart>
    </div>    
</template>
  
<script>
    export default {
    name: 'DateCorrectness',
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
                labels: ['Correcte datums']
            },
            series: [],
        }
    },
    beforeMount() {
        
    },
    methods: {
        async setDateCorrectness() {
            
            this.series = [this.data.correctness.dateCorrectness];
        },       
    },
    watch: {
        data: function(value) {
            this.setDateCorrectness();
        }
    }
}
</script>

<style>

</style>
