<template>
  <div class="container">
    <h3>서울 날씨</h3>
    <weather />
    <hr>
    <h3>Led 상태</h3>
    <hr>
    <div class="row">
      <div v-for="(led,ix) in leds" :key="ix" class="col-4">
        <led :index="ix" :place="led.place" :color="led.color"
            :state="led.state" @led-state-change="onLedStateChange"/>
      </div>
    </div>
  </div>
</template>

<script>
import Led from '@/components/Led.vue';
import Weather from '@/components/Weather.vue';

export default {
  name: 'ComponentExample',
  components: { Led, Weather }, // Local Component
  data() {
    return {
      leds: [ // 나중에 mqtt로 받기
        { place: '거실', color: 'red', state: false },
        { place: '부엌', color: 'green', state: true },
        { place: '침실', color: 'blue', state: false },
      ]
    };
  },
  methods: {
    onLedStateChange(index, state) {
      this.leds[index].state = state;
    }
  },
}
</script>

<style scoped>

</style>
