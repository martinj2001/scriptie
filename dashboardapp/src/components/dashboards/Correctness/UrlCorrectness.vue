<template>
    <div id='urlcorrectness'>
      <apexchart type="radialBar" height="350" :options="options" :series="series"></apexchart>
    </div>    
</template>
  
<script>
    export default {
    name: 'UrlCorrectness',
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
                labels: ['Correcte url\'s']
            },
            series: [],
        }
    },
    beforeMount() {
        
    },
    methods: {
        async setUrlCorrectness() {
            
            this.series = [this.data.correctness.urlCorrectness];
        },       
    },
    watch: {
        data: function(value) {
            this.setUrlCorrectness();
        }
    }
}
</script>

<style>

</style>
