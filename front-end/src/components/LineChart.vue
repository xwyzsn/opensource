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
  }
})

onMounted(()=>{
  let chart = echarts.init(document.getElementById(props.cid));
  let option = {
      title:{
        text: props.title
      },
      xAxis: {
        type: 'category',
        data: props.data.map((item)=>item.x).slice(1,)
      },
      yAxis: {
        type: 'value'
      },
      series: [
        {
          data: props.data.map((item)=>item.y).slice(1,),
          type: 'line'
        }
      ],
};
  console.log(props.data.x)
  chart.setOption(option);
})
</script>

<template>
<div class="w-full h-full" :id="props.cid">

</div>
</template>

<style scoped>

</style>