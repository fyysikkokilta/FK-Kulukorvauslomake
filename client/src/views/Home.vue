<template>
  <div>
    <router-view />
    <b-tabs>
      <b-tab title="Kulukorvauslomake" active>
        <CostForm/>
      </b-tab>
      <b-tab title="Matkakorvauslomake">
        <TravelForm/>
      </b-tab>
    </b-tabs>
  </div>
</template>

<script>
import TravelForm from '@/components/TravelForm.vue';
import CostForm from '@/components/CostForm.vue';

export default {
  name: 'home',
  components: {
    TravelForm,
    CostForm,
  },
};
</script>
