<template>
  <div>
    <router-view />
    <b-tabs>
      <b-tab title="Kulukorvaus" active>
        <CostForm/>
      </b-tab>
      <b-tab title="Matkakorvaus">
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
