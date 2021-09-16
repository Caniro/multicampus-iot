import Vue from 'vue';

import Weather from '../components/Weather'
import PageTitle from '../components/ui/PageTitle'
import MTitle from '../components/ui/MTitle'
import Temperature from '../components/sensors/Temperature'
import Humidity from '../components/sensors/Humidity'
import Illumination from '../components/sensors/Illumination'

Vue.component('PageTitle', PageTitle)
Vue.component('Weather', Weather)
Vue.component('MTitle', MTitle)
Vue.component('Temperature', Temperature)
Vue.component('Humidity', Humidity)
Vue.component('Illumination', Illumination)
