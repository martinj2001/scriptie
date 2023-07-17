<template>
    <div id='readibilityPerColumn'>
        <apexchart type="bar" height="700" :options="options" :series="series"></apexchart>
    </div>    
</template>
  
<script>
    export default {
    name: 'ReadibilityColumn',
    props: {
        data: Object
    },
    data() {
        return {            
            options: {
        chart: {
          height: 700,
          width: 50,
          type: 'bar'
        },
        colors: ['#154273'],
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
            text: 'Kolom'
          },
          labels: {
            rotate: -45,
            style: {
              fontSize: '10px'
            },
            trim: true,
            hideOverlappingLabels: false,
            maxHeight: 150,
          },
          tickPlacement: 'on'
        },
        yaxis: {
          title: {
            text: 'Percentage leesbare teksten'
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
          name: 'Percentage leesbare teksten per kolom',
          data: []
        }
      ],
    }
    },
    beforeMount() {
        
    },
    methods: {
        async setData() {
            this.options = {
        xaxis: {          
          categories: Object.keys(this.data.accessibility.readabilityPerColumn),
      }
      };
      this.series = [{
        data: Object.values(this.data.accessibility.readabilityPerColumn)
      }]
        }     
    },
    watch: {
        data: function(value) {          
            this.setData()
        }
    }
}
</script>

<style>

</style>
