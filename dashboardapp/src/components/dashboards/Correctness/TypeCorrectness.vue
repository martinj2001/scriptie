<template>
    <div id='typecorrectness'>
      <apexchart type="radialBar" height="350" :options="options" :series="series"></apexchart>
    </div>    
</template>
  
<script>
    export default {
    name: 'TypeCorrectness',
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
                labels: ['Correcte algoritmetypes']
            },
            series: [],
        }
    },
    beforeMount() {
        
    },
    methods: {
        async setTypeCorrectness() {
            
            this.series = [this.data.correctness.typeCorrectness];
        },       
    },
    watch: {
        data: function(value) {
            this.setTypeCorrectness();
        }
    }
}
</script>

<style>

</style>
