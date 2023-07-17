<template>
    <div id='readibilityOveral'>
      <apexchart type="radialBar" height="350" :options="options" :series="series"></apexchart>
    </div>    
</template>
  
<script>
    export default {
    name: 'ReadibilityOverall',
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
                labels: ['Leesbaarheid (FRE)']
            },
            series: [],
        }
    },
    beforeMount() {
        
    },
    methods: {
        async setReadibilityData() {
            
            this.series = [this.data.accessibility.readability];
        },       
    },
    watch: {
        data: function(value) {
            this.setReadibilityData();
        }
    }
}
</script>

<style>

</style>
