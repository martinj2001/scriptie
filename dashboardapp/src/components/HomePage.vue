<template>
  <div>
    <h2>Home Page</h2>
    <div id='completenessTotal'>
      <apexchart type="radialBar" height="350" :options="completenessTotalOptions" :series="completenessTotalSeries"></apexchart>
    </div>

    <div id='completenessPerOrganisation'>
      <apexchart type="bar" height="700" width="1000" :options="completePerOrganizationOptions" :series="completenessPerOrganizationSeries"></apexchart>
    </div>

    <div id='completenessColumn'>
        <apexchart type="bar"  height="700" width="1000" :options="completePerColumnOptions" :series="completenessPerColumnSeries"></apexchart>
    </div>

    <CompleteOrganization :data-quality="data"/>
  </div>
  
  
</template>

<script>
import CompleteOrganization from './CompleteOrganization.vue';
export default {
  name: 'HomePage',
  components: {
    CompleteOrganization
  },
  data() {
    return {
      data: {bla:'bla'},
      completenessTotalOptions: {
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
      completenessTotalSeries: [],
      completePerOrganizationOptions: {
        chart: {
          height: 700,
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
        }
        }
      },
      completePerColumnOptions: {
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
            text: 'Kolomnaam'
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
      completenessPerOrganizationSeries: [
        {
          name: 'Percentage lege velden',
          data: []
        }
      ],
      completenessPerColumnSeries: [
        {
          name: 'Percentage lege velden',
          data: []
        }
      ]
    }
  },
  async beforeMount() {
    await this.getAlgorithmsData();
  },
  methods: {
    async getAlgorithmsData() {
      try {
        const response = await this.$http.get(process.env.VUE_APP_API_URL + '/algorithms/score');
        this.data = response.data;
        console.log(JSON.parse(JSON.stringify(response.data)))
        this.setGraphData();
      } catch(error) {
        console.log(error);
      }
    },
    async setGraphData() {
      this.setCompletenessTotal();
      this.setCompletenessPerOrganization();
      this.setCompletenessPerColumn();
    },
    async setCompletenessTotal() {
      this.completenessTotalSeries = [this.data.completeness.emptyValuesPercentage];
    },
    async setCompletenessPerOrganization() {
      this.completePerOrganizationOptions = {
        xaxis: {          
          categories: Object.keys(this.data.completeness.emptyValuesPerOrganisation),
      }
      };
      this.completenessPerOrganizationSeries = [{
        data: Object.values(this.data.completeness.emptyValuesPerOrganisation)
      }]
    },
    async setCompletenessPerColumn() {
      this.completePerColumnOptions = {
        xaxis: {          
          categories: Object.keys(this.data.completeness.emptyValuesPerColumn),
      }
      };
      this.completenessPerColumnSeries = [{
        data: Object.values(this.data.completeness.emptyValuesPerColumn)
      }]
    }
  }
}
</script>

<style scoped>
div.chart-wrapper {
  display: block;
  align-items: center;
  justify-content: center
}

#completenessPerOrganisation, #completenessColumn {
  display: inline-block;
}

</style>