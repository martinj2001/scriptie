<template>
    <div id='emailcorrectmess'>
      <apexchart type="radialBar" height="350" :options="options" :series="series"></apexchart>
    </div>    
</template>
  
<script>
    export default {
    name: 'EmailCorrectness',
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
                labels: ['Correcte e-mailadressen']
            },
            series: [],
        }
    },
    beforeMount() {
        
    },
    methods: {
        async setEmailCorrectness() {
            
            this.series = [this.data.correctness.emailCorrectness];
        },       
    },
    watch: {
        data: function(value) {
            this.setEmailCorrectness();
        }
    }
}
</script>

<style>

</style>
