<template>
  <div class="chart-wrapper">
    <apexchart 
      width="800" 
      type="bar" 
      :options="options" 
      :series="series">
    </apexchart>

    <apexchart
      width="400"
      type="radialBar"
      :options="optionsRadial"
      :series="seriesRadial">
    </apexchart>
</div>
</template>

<script>
import Data from '@/data/data.json';

export default {
  name: 'HelloWorld',
  data: () => ({
    options: {
      chart: {
        id: 'vuechart-example'
      },
      xaxis: {
        categories: [
         "Jan",
         "Feb",
         "Mar",
         "Apr",
         "May",
         "Jun",
         "Jul",
         "Aug",
         "Sep",
         "Oct",
         "Nov",
         "Dec"
        ]
      }
    },
    series: [{
      name: 'series-1',
      data: [55, 62, 89, 66, 98, 72, 101, 75, 94, 120, 117, 139]
    }],
    optionsRadial: {
      chart: {
        id : 'vuechart-example2',
        type: 'radialBar',
        height: 100,
        width: 200,
      },
      labels: ['Lege velden %'],
      
    },
    seriesRadial: [70],
    
    
  }),
  methods: {
    getPercentageOfEmptyFields: function() {
      let emptyCount = 0;
      let totalCount = 0;
      
      for(var i in this.data)
      {
        for(var [k,v] of Object.entries(this.data[i]))
        {
          if(v == "" || v == undefined)
          {
            emptyCount++;
          }
          totalCount++;
        }
      }
      return Math.round((emptyCount/totalCount * 100)) 
    }
    
  },
  mounted: function() {
      this.data = Data;
      this.seriesRadial = [this.getPercentageOfEmptyFields()]
  }}
</script>

<style scoped>
div.chart-wrapper {
  display: block;
  align-items: center;
  justify-content: center
}
</style>