<script setup>
import {api} from "../../api/api";
import {onMounted, ref} from "vue";
import RelationGraph from "@/components/RelationGraph.vue";
let data = ref(null)
api.get("/get_all_user_repo_or").then(res=>{
  data.value = res.data;
  console.log(data.value)
})
</script>

<template>
<div class="w-full h-full">
<RelationGraph v-if="data !==null" :data="data" cid="relation-graph" class="w-full h-full"></RelationGraph>
</div>
</template>

<style scoped>

</style>