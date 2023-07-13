<script setup>
import {api} from "../../api/api";
import {ref, onMounted, reactive} from "vue";
import {useRoute,useRouter} from "vue-router";
import {setUserAllRepo} from "../../api/api";
import SanKey from "@/components/SanKey.vue";
import BarChart from "@/components/BarChart.vue";
let userAllRepo = ref([]);
let searchInput = ref("alibaba");
const query = useRoute().query;
const router = useRouter();
searchInput.value = query.repo;
let maxScore = reactive({
  value: 0,
  name:''
});
let unfold = ref(false)
const searchAll = (user)=>{
  setUserAllRepo(user).then(res=>{
    userAllRepo.value = res.data;
    userAllRepo.value.forEach(item=>{
      if(item.or>maxScore.value){
        maxScore.value = item.or;
        maxScore.name = item.n;
      }
    })
  })
}
searchAll(searchInput.value);


</script>

<template>
<div class="w-full h-full">
  <div class="h-20 w-full bg-zinc-100">
    <div class="w-full h-full flex justify-start space-x-3">
      <div class="m-5 flex ">
      <el-input disabled placeholder="User" v-model="searchInput" class="w-1/2"></el-input>
        <el-button type="primary" class="ml-3 mt-1" @click="()=>{searchAll(searchInput)}">Search</el-button>
      </div>
    </div>
  </div>
  <div class="h-full w-full grid-cols-3 grid ">
    <div class="w-full h-full col-span-2">
      <san-key class="w-full h-full  max-w-6xl overflow overflow-x-scroll " v-if="userAllRepo.length>0" :data="userAllRepo" cid="sankey1" :source="searchInput"></san-key>
    </div>
    <div class="w-full h-full col-span-1">
      <div class="grid grid-rows-6 h-full">
        <div class="row-span-1 w-full h-full">
          <el-statistic title="Activate repo number" :value="userAllRepo.length" />
          <el-statistic title="Highest score of openrank" :value="maxScore.value" />
          <el-statistic title="Highest repo " :value="maxScore.name" />
        </div>
        <div class="row-span-2 ">
          <bar-chart v-if="userAllRepo.length>0" class="w-full h-full" :data="userAllRepo" cid="barChart" />
        </div>
        <div class="row-span-3 w-full h-full ">
          <div class="mt-2 text-xl">
            All activate repo
          </div>
            <el-collapse class="h-52 overflow-y-scroll" v-model="unfold" accordion>
              <el-collapse-item v-for="(item,idx) in userAllRepo.sort((a,b)=>{return b.or-a.or})" :title="item.n">
                <div class="pl-3">
                  openrank: {{item.or}}
                  <br>
                  ranking: {{idx+1}}
                  <br>
                  <el-button type="primary" class="mt-2" @click="()=>{
                    router.push({
                      name:'repo',
                      query:{
                        repo:item.n,
                        company:searchInput
                      }
                    })
                  }">Go to repo panel</el-button>
                </div>
              </el-collapse-item>
            </el-collapse>
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<style scoped>

</style>