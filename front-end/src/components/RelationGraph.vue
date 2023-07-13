<script setup>
import {onMounted, ref, watch} from "vue";
import * as echarts from 'echarts';
import {useRouter} from "vue-router";
const router = useRouter()
const props = defineProps({
  data: {
    type: Object,
    default: {}
  },
  cid: {
    type: String,
    default: ""
  },
  selected:{
    type:Boolean,
    default: false

  }
})
watch(()=>props.data,(newVal,oldValue)=>{
  console.log(newVal)
    let chart = echarts.getInstanceByDom(document.getElementById(props.cid))
  let option = {
    animationDurationUpdate: 500,
    animationEasingUpdate: 'quinticInOut',
            legend: [
          {
            data: props.data.category.map(function (a) {
              return a.name;
            }),
            type:'scroll',
            selectedMode: 'multiple',
            selected: props.data.category.reduce(function (obj, item) {
              obj[item.name] = props.selected;
              return obj;
            }, {})
          }
        ],
    series: [
      {
        type: 'graph',
        layout: 'force',
        symbolSize: 50,
        roam: true,
        label: {
          show: true
        },
        data: props.data.nodes,
        links: props.data.links,
        force: {
          repulsion: 1000
        },
        lineStyle: {
          opacity: 0.9,
          width: 2,
          curveness: 0
        },
        categories: props.data.category,
      }
    ]
  };
  chart.setOption(option)
})
onMounted(() => {
  let chart = echarts.init(document.getElementById(props.cid))
  let option = {
    animationDurationUpdate: 500,
    animationEasingUpdate: 'quinticInOut',
            legend: [
          {
            data: props.data.category.map(function (a) {
              return a.name;
            }),
            type:'scroll',
            selectedMode: 'multiple',
            selected: props.data.category.reduce(function (obj, item) {
              obj[item.name] = props.selected;
              return obj;
            }, {})
          }
        ],
    series: [
      {
        type: 'graph',
        layout: 'force',
        symbolSize: 50,
        roam: true,
        label: {
          show: true
        },
        data: props.data.nodes,
        links: props.data.links,
        force: {
          repulsion: 1000
        },
        lineStyle: {
          opacity: 0.9,
          width: 2,
          curveness: 0
        },
        categories: props.data.category,
      }
    ]
  };
  chart.setOption(option)
  chart.on('click', function (params) {
    if(params.dataType === 'node'){
      if(params.data.category === params.data.name){
        router.push({
          name:'dashboard',
          query:{
            repo:params.data.name,
          }
        })
      }
    }
  })
})
</script>

<template>
  <div class="w-full h-full" :id="props.cid">

  </div>

</template>

<style scoped>

</style>