<template>
    <div id='completenessOrganization'>
        <apexchart type="bar" height="700" :options="options" :series="series"></apexchart>
    </div>    
</template>
  
<script>
    export default {
    name: 'CompleteOrganization',
    props: {
        data: {
            type: Object
        },        
    },
    data() {
        return {            
            options: {
              colors: ['#154273'],
        chart: {
          
          height: 700,
          width: 50,
          type: 'bar'
        },
        plotOptions: {
          bar: {
            horizontal: false,
            columnwidth: '55%',
          }
        },
        dataLabels: {
          enabled: false,
          formatter: function(val) {
            return val + '%';
          },
          style: {
            fontSize: '10px'
          }
        },
        stroke: {
          show: true,
          width: 2,
          colors: ['transparent']
        },
        xaxis: {
          title: {
            text: 'Organisatie'
          },
          labels: {
            rotate: -45,
            rotateAlways: true,
            style: {
              fontSize: '10px'
            },
            trim: true,
            hideOverlappingLabels: false,
            maxHeight: 300,
          },
          tickPlacement: 'on'
        },
        yaxis: {
          title: {
            text: 'Percentage lege velden per kolom'
          },
          labels: {
            formatter: function(val) {
              return val + '%';
            }
          },
          max: 100
        },
        fill: {
          opacity: 1
        },
        tooltip: {
          y: {
            formatter: function(val) {
              return val + '%'
            }
        }
        }
      },
      series: [
        {
          name: 'Percentage lege velden',
          data: []
        }
      ],
    }},
    mounted() {                       
    },
    methods: {
        async setData() {
            this.options = {
        xaxis: {          
          categories: Object.keys(this.data.completeness.emptyValuesPerOrganisation),
      }
      };
      this.series = [{
        data: Object.values(this.data.completeness.emptyValuesPerOrganisation)
      }]
        },       
    },
    watch: {
        data: function(value) {
            this.setData();
        }
    }
}
    
</script>

<style>

</style>
