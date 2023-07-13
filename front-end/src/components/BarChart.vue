<script setup>
import * as echarts from 'echarts';
import {ref, onMounted, watch} from "vue";

const props = defineProps({
  data: {
    type: Array,
    default: () => []
  },
  cid: {
    type: String,
    default: ""
  }
})

let x = ref([]);
let y = ref([]);
props.data.forEach(item=>{
  x.value.push(item.n);
  y.value.push(item.or);
})
watch(()=>props.data,(newVal,oldVal)=>{
  x.value = [];
  y.value = [];
  newVal.forEach(item=>{
    x.value.push(item.n);
    y.value.push(item.or);
  })
  let chart = echarts.getInstanceByDom(document.getElementById(props.cid));
   let option = {
    xAxis: {
      type: 'category',
      data: x.value,
      axisLabel:{
        interval:0,
        rotate:90,
        textAlign:'right',
        marginBottom:100,
        marginRight:100
      }
    },
    yAxis: {
      type: 'value'
    },
    series: [
      {
        data: y.value,
        type: 'bar'
      }
    ]
  };
  if(chart !== void 0){
    chart.setOption(option);
  }
})
onMounted(() => {
  let chart = echarts.init(document.getElementById(props.cid));
  let option = {
    xAxis: {
      type: 'category',
      data: x.value,
      axisLabel:{
        interval:0,
        rotate:90,
        textAlign:'right',
        marginBottom:100,
        marginRight:100
      }
    },
    yAxis: {
      type: 'value'
    },
    series: [
      {
        data: y.value,
        type: 'bar'
      }
    ]
  };
  chart.setOption(option);
})
</script>

<template>
  <div class="w-full h-full">
    <div class="w-full h-full" :id="props.cid">

    </div>
  </div>
</template>

<style scoped>

</style>