<template>
    <div id='completenessOrganization'>
      <apexchart type="radialBar" height="350" :options="options" :series="series"></apexchart>
    </div>    
</template>
  
<script>
    export default {
    name: 'CompleteOrganization',
    props: {
        dataQuality: {
            type: Object
        }
    },
    data() {
        return {            
            options: {
                chart: {
                    height: 700,
                    type: 'bar',
                    type2: this.dataQuality
                },
                plotOptions: {
                    bar: {
                        horizontal: false,
                        columnwidth: '55%',
                    }
                },
                dataLabels: {
                    enabled: true,
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
                text: 'Percentage lege velden per organisatie'
            },
            labels: {
                formatter: function(val) {
                return val + '%';
                }
            }
            },
            fill: {
            opacity: 1
            },
            tooltip: {
            y: {
                formatter: function(val) {
                return val + '%'
                }
            }}
      },
      series: [
        {
          name: 'Percentage lege velden',
          data: []
        }
      ],
    }},
    mounted() {
        console.log(this.dataQuality);
        this.setCompletenessTotal();
    },
    methods: {
        async setCompletenessTotal() {
            this.series = [this.dataQuality.completeness.emptyValuesPercentage];
        },       
    }
}
    
</script>

<style>

</style>
