<template>
  <div>
    <ul class="mt-3">
      <li v-for="(file, ix) in fileList" :key="ix" @click="video=file">
        {{ file.name }}
      </li>
    </ul>
    <v-img :src="video.url" />
  </div>
</template>

<script>
export default {
  name: 'VideoList',
  data() {
    return {
      video: {},
      fileList: [
        { name: 'video1.mp4', url: 'https://picsum.photos/640/480?random=5'},
        { name: 'video2.mp4', url: 'https://picsum.photos/640/480?random=6'},
        { name: 'video3.mp4', url: 'https://picsum.photos/640/480?random=7'},
        { name: 'video4.mp4', url: 'https://picsum.photos/640/480?random=8'},
      ]
    }
  }
}
</script>

<style>

</style>