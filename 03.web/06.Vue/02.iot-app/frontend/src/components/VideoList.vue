<template>
  <div>
    <v-btn class="float-right" color="primary" 
          @click="load" icon><v-icon>mdi-refresh</v-icon></v-btn>
    <ul class="mt-3">
      <li v-for="(file, ix) in fileList" :key="ix" @click="video=file">
        {{ file.filename }}
      </li>
    </ul>
    <video v-if="video.video_file" :src="video.video_file" 
          class="video" controls autoplay></video>
  </div>
</template>

<script scoped>
import axios from 'axios';

export default {
  name: 'VideoList',
  data() {
    return {
      video: {},
      fileList: [
      ]
    }
  },
  methods: {
    async load() {
      try {
        const { data } = await axios.get('/api/video');
        console.log(data.results)
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
.video {
  max-width: 100%;
}
</style>
