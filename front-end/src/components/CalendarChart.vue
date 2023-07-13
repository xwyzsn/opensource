<script setup>
import * as echarts from 'echarts';
import {onMounted, ref} from "vue";
const props = defineProps({
  data: {
    type: Array
  },
  cid:{
    type: String,
    default: () => ''
  },
  title:{
    type: String,
    default: () => ''
  },
  month:{
    type: String,
  }
})
let option = ref({
  tooltip: {
    trigger: 'item',
    formatter: '{a} <br/>{b}: {c} ({d}%)'
  },
  visualMap: {
    show: false,
    min: 0,
    max: 600,
    calculable: true,
    orient:'horizontal',
    left: 'center',
    bottom: '15%'
  },
  calendar: {
    range: props.month,
    cellSize: ['auto', 20],
  },
  series:[
    {
      type:'heatmap',
      coordinateSystem: 'calendar',
      data: props.data
    }
  ]
})
onMounted(() => {
    let chart = echarts.init(document.getElementById(props.cid));
    chart.setOption(option.value);
    }
)


</script>

<template>
<div class="w-full h-full" :id="props.cid">

</div>
</template>

<style scoped>

</style>