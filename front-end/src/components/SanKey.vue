<script setup>
import * as echarts from 'echarts';
import {onMounted, ref, watch} from "vue";

const props = defineProps({
  data: {
    type: Array,
    default: () => []
  },
  cid: {
    type: String,
    default: ""
  },
  source: {
    type: String
  }
})

let links = ref([])
let node = ref([])
let source = ref(props.source)
let nodeSet = new Set()

function checkIfContainNode(name) {
  let flag = false;
  node.value.forEach(item => {
    if (item.name === name) {
      flag = true;
    }
  })
  return flag;
}

watch(() => props.source, (newVal, oldVal) => {
  source.value = newVal
})
watch(() => props.data, (newVal, oldVal) => {
  node.value = []
  links.value = []
  node.value.push({
    name: source.value
  })
  newVal.forEach(item => {
    if (!checkIfContainNode(item.n)) {
      node.value.push({
        name: item.n
      })
    }
    links.value.push({
      source: source.value,
      target: item.n,
      value: item.or
    })
  })
  console.log(node.value)


  let myChart = echarts.getInstanceByDom(document.getElementById(props.cid));
  let option = {
    series: {
      type: 'sankey',
      layout: 'none',
      emphasis: {
        focus: 'adjacency'
      },
      data: node.value,
      links: links.value,
      orient: 'vertical',
      label: {
        position: 'top',
        interval: 0,
        rotate: 90,
        margin: 100,
        textAlign: 'right',
      },

    }
  };
  if (myChart) {
    myChart.setOption(option);
  }
})
props.data.forEach(item => {
  if (!nodeSet.has(item.n)) {
    node.value.push({
      name: item.n
    })
    nodeSet.add(item.n)
  }

  links.value.push({
    source: props.source,
    target: item.n,
    value: item.or
  })
})
if(!nodeSet.has(props.source)){
  node.value.push({
    name: props.source
  })
  nodeSet.add(props.source)
}

onMounted(() => {
  let myChart = echarts.init(document.getElementById(props.cid));
  let option = {
    series: {
      type: 'sankey',
      layout: 'none',
      emphasis: {
        focus: 'adjacency'
      },
      data: node.value,
      links: links.value,
      orient: 'vertical',
      label: {
        position: 'top',
        interval: 0,
        rotate: 90,
        margin: 100,
        textAlign: 'right',
      },

    }
  };
  myChart.setOption(option);

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