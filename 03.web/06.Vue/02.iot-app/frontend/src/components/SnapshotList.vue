<template>
  <div>
    <v-btn class="float-right" color="primary" 
      @click="load" icon><v-icon>mdi-refresh</v-icon></v-btn>
    <ul class="mt-3">
      <li v-for="(file, ix) in fileList" :key="ix" @click="image=file"
        :class="{active: image===file}">
        {{ file.filename }}
      </li>
    </ul>
    <v-img :src="image.image_file" />
  </div>  
</template>

<script scoped>
import axios from '@/util/api';

export default {
  name: 'SnapshotList',
  data() {
    return {
      image: {}, // 클릭한 이미지
      fileList: [
      ]
    }
  },
  methods: {
    async load() {
      try {
        const { data } = await axios.get('/api/snapshot');
        this.fileList = data.results;
      } catch(e) {
        console.log('에러: ', e);
      }
    }
  },
  async mounted() {
    this.load()
  }
}
</script>

<style scoped>
.active {
  color: red;
  font-weight: bold;
}
</style>