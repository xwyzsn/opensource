<script setup>
import {ref, onMounted} from "vue";
import * as echarts from 'echarts';

const props = defineProps({
  data: {
    type: Object,
    required: true
  }
})
onMounted(() => {
  let dom = document.getElementById("circle-group")
  let myChart = echarts.init(dom);
  const gaugeData = [
    {
      value: 20,
      name: 'Perfect',
      title: {
        offsetCenter: ['-40', '-20%']
      },
      detail: {
        valueAnimation: true,
        offsetCenter: ['17%', '-20%']
      }
    },
    {
      value: 40,
      name: 'Good',
      title: {
        offsetCenter: ['-40', '10%']
      },
      detail: {
        valueAnimation: true,
        offsetCenter: ['17%', '10%']
      }
    },
    {
      value: 60,
      name: 'Commonly',
      title: {
        offsetCenter: ['-40', '40%']
      },
      detail: {
        valueAnimation: true,
        offsetCenter: ['17%', '40%']
      }
    }
  ];
  let option = {
    series: [
      {
        type: 'gauge',
        startAngle: 90,
        endAngle: -270,
        pointer: {
          show: false
        },
        progress: {
          show: true,
          overlap: false,
          roundCap: true,
          clip: false,
          itemStyle: {
            borderWidth: 1,
            borderColor: '#464646'
          }
        },
        axisLine: {
          lineStyle: {
            width: 40
          }
        },
        splitLine: {
          show: false,
          distance: 0,
          length: 10
        },
        axisTick: {
          show: false
        },
        axisLabel: {
          show: false,
          distance: 50
        },
        data: gaugeData,
        title: {
          fontSize: 14
        },
        detail: {
          width: 50,
          height: 14,
          fontSize: 14,
          color: 'inherit',
          borderColor: 'inherit',
          borderRadius: 20,
          borderWidth: 1,
          formatter: '{value}%'
        }
      }
    ]
  };

  option && myChart.setOption(option);

})

</script>

<template>
  <div class="w-full h-full">
    <div id="circle-group" class="w-full h-full">

    </div>
  </div>
</template>

<style scoped>

</style>