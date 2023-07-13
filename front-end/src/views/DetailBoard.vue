<script setup>
import {useRoute} from "vue-router";
import {api} from "../../api/api";
import {reactive, ref, watch} from "vue";
import {Link} from "@element-plus/icons-vue"
import LineChart from "@/components/LineChart.vue";
import NodeChart from "@/components/NodeChart.vue";
import RelationGraph from "@/components/RelationGraph.vue";

const route = useRoute()
const query = route.query
let repoName = query.repo;
let company = query.company;
let data = ref(null)
let month = ref('')
let monthOptions = ref([])
let selectedData = reactive({
  busFactor: [],
  openRank: []
})
watch(month, (newVal, oldValue) => {
  console.log(newVal)
  if (data.value) {
    selectedData.busFactor = data.value[month.value].bus_factor_detail
    selectedData.openRank = data.value[month.value].activity_details
  }
})
let statistic = reactive({
  star: [{x: null, y: 0}],
  fork: [{x: null, y: 0}],
})
api.get(`/get_all_info_of_repo/${company}/${repoName}`).then(res => {
  data.value = res.data
  month.value = Object.keys(data.value)[0]
  monthOptions.value = Object.keys(data.value)
  console.log(data.value)
  for (let [k, v] of Object.entries(data.value)) {
    statistic.star.push({x: k, y: v.stars + (+statistic.star[statistic.star.length - 1].y)})
    statistic.fork.push({x: k, y: v.technical_fork + (+statistic.fork[statistic.fork.length - 1].y)})
  }
})
let userRepo = ref(null)
const getUserRepos=(user)=>{
  api.get(`/user_repo/${user}`).then(res=>{
    userRepo.value = res.data
    console.log(userRepo.value)
  })
}
const openUrl = () => {
  window.open(`https://github.com/${company}/${repoName.replace(/repo:/g, "")}`)
}


</script>

<template>
  <div class="w-full h-full bg-white">
    <div class="flex h-1/3 w-full space-x-3 p-2 mt-5 ">
      <div class="w-1/3 h-full bg-zinc-50 rounded-2xl ">
        <line-chart v-if="statistic.star.length>1" class="w-full h-full" :data="statistic.star" cid="starChart"
                    title="start Increase"/>
      </div>
      <div class="w-1/3 h-full bg-zinc-50 rounded-2xl">
        <line-chart v-if="statistic.fork.length > 1" class="w-full h-full" :data="statistic.fork" cid="forkChart"
                    title="fork Increase"/>
      </div>
      <div class="w-1/3 h-full bg-zinc-50 rounded-2xl">
        <div class="flex justify-around mt-5">
          <el-statistic title="total star " :value="statistic.star[statistic.star.length-1].y"></el-statistic>
          <el-statistic title="total fork " :value="statistic.fork[statistic.fork.length-1].y"></el-statistic>
        </div>
        <div class="text-2xl flex justify-center mt-5">
          Repo:{{ repoName.replace(/repo:/g, "") }}
          <el-icon>
            <Link class="cursor-pointer" @click="openUrl"/>
          </el-icon>
        </div>
        <div class="flex justify-center mt-2 ">
          <el-select v-model="month">
            <el-option v-for="item in monthOptions" :key="item" :label="item" :value="item"></el-option>
          </el-select>
        </div>
        <div class="flex justify-around mt-5">
          <!--      <el-statistic title="core member of this month" :value=""></el-statistic>-->
          <!--      <el-statistic title="Most activate of this month " :value=""></el-statistic>-->
        </div>
      </div>
    </div>
    <div class="flex h-2/3 w-full space-x-3 pt-2 mt-5">
      <div class="w-1/3 h-full bg-zinc-50 rounded-2xl">
        <node-chart v-if="selectedData.busFactor.length > 0"
                    :title="'bus factor of ' + month"
                    cid="bus-factor"
                    @click-node="(user)=>{getUserRepos(user)}"
                    :data="selectedData.busFactor"
        />
      </div>
      <div class="w-1/3 h-full bg-zinc-50 rounded-2xl">
        <node-chart v-if="selectedData.openRank.length > 0"
                    :title="'Activity of ' + month"
                    cid="activity"
                    @click-node="(user)=>{getUserRepos(user)}"
                    :data="selectedData.openRank"
        />
      </div>
      <div class="w-1/3 h-full bg-zinc-50 rounded-2xl">
        <relation-graph v-if="userRepo" :data="userRepo" cid="uid" :selected="true"/>
        <div v-else>
          <div class="flex justify-center items-center align-middle ">
            <div>
              <div class="text-2xl">click user and see his repo network</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>

</style>