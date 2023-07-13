<script setup>
import * as echarts from 'echarts';
import {onMounted, ref, watch} from "vue";
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

const emits = defineEmits(['clickNode'])
const randomColor = () => {
  return '#'+Math.floor(Math.random()*0xffffff).toString(16);
}
onMounted(()=>{
  let chart = echarts.init(document.getElementById(props.cid));
  let option ={
        title: {
          text: props.title
        },
        animationDurationUpdate: 1500,
        animationEasingUpdate: 'quinticInOut',
        series: [
          {
            type: 'graph',
            layout: 'force',
            force: {
              repulsion: 100
            },
            data: props.data.map(function (node,index) {
              return {
                id: index,
                name: 'name:'+ node[0]+'\nbus-factor:'+node[1],
                symbolSize: node[1]*10,
                itemStyle: {
                  color: randomColor()
                },
              };
            }),
            emphasis: {
              focus: 'adjacency',
              label: {
                position: 'right',
                show: true
              }
            },
            roam: true,
            lineStyle: {
              width: 0.5,
              curveness: 0.3,
              opacity: 0.7
            }
          }
        ]
  };
  chart.setOption(option);
  chart.on('click',(param)=>{
    if(param.dataType === 'node'){
      let user = param.data.name.split('\n')[0].split(':')[1];
      emits('clickNode',user)
      // window.open(`https://github.com/${user}`)
    }
  })
})
watch(()=>props.data,(newVal,oldValue)=>{
  let chart = echarts.getInstanceByDom(document.getElementById(props.cid));
  let option ={
        title: {
          text: props.title
        },
        animationDurationUpdate: 1500,
        animationEasingUpdate: 'quinticInOut',
        series: [
          {
            type: 'graph',
            layout: 'force',
            force: {
              repulsion: 100
            },
            data: props.data.map(function (node,index) {
              return {
                id: index,
                name: 'name:'+ node[0]+'\nbus-factor:'+node[1],
                symbolSize: node[1]*10,
                itemStyle: {
                  color: randomColor()
                },
              };
            }),
            emphasis: {
              focus: 'adjacency',
              label: {
                position: 'right',
                show: true
              }
            },
            roam: true,
            lineStyle: {
              width: 0.5,
              curveness: 0.3,
              opacity: 0.7
            }
          }
        ]
  };
  chart.setOption(option);
})
</script>

<template>
<div class="w-full h-full" :id="props.cid">

</div>
</template>

<style scoped>

</style>