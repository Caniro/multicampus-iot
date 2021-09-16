<template>
  <div>
    <page-title icon="mdi-access-point-network">MQTT 모니터링</page-title>

    <div class="my-3">
      <div v-for="(devices, place) in sensors" :key="place">
        <m-title icon="fas fa-map-marker-alt">{{ place }}</m-title>
        <hr class="mt-1 mb-3">
        <v-row>
          <v-col class="pa-3" cols="12" sm="4"
                v-for="(value, device) in devices" :key="device">
            <temperature v-if="device==='temp'" :value="value"></temperature>
            <humidity v-if="device==='humi'" :value="value"></humidity>
            <illumination v-if="device==='illu'" :value="value"></illumination>
          </v-col>
        </v-row>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Mqtt',
  data() {
    return {
      sensors: {
        bedroom: {
          temp: 20.5,
          humi: 24,
          illu: 20
        },
        room1: {
          temp: 100,
          humi: 100,
          illu: 100
        }
      }
    };
  },
  mqtt: {
    'iot/hong/sensors/#': function(value, topic) {
      const [,,,place, device] = topic.split('/');
      
      if (!this.sensors[place]) // 처음 받은 장소 초기화
        this.sensors[place] = {};
      this.sensors[place][device] = value;
    }
  },
  mounted() {
    this.$mqtt.subscribe('iot/hong/sensors/#');
  },
  unmounted() {
    this.$mqtt.unsubscribe('iot/hong/sensors/#');
  },
}
</script>

<style>

</style>