<template>
  <div>
    <ul class="mt-3">
      <li v-for="(file, ix) in fileList" :key="ix" @click="image=file">
        {{ file.filename }}
      </li>
    </ul>
    <v-img :src="image.image_file" />
  </div>  
</template>

<script scoped>
import axios from 'axios';

export default {
  name: 'SnapshotList',
  data() {
    return {
      image: {}, // 클릭한 이미지
      fileList: [
        // { name: 'picture1.jpg', url: 'https://picsum.photos/640/480?random=1'},
        // { name: 'picture2.jpg', url: 'https://picsum.photos/640/480?random=2'},
        // { name: 'picture3.jpg', url: 'https://picsum.photos/640/480?random=3'},
        // { name: 'picture4.jpg', url: 'https://picsum.photos/640/480?random=4'},
      ]
    }
  },
  async mounted() {
    try {
      const { data } = await axios.get('/api/snapshot');
      this.fileList = data.results;
    } catch(e) {
      console.log('에러: ', e);
    }
  }
}
</script>

<style>

</style>