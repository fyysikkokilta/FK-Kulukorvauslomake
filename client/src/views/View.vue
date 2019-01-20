<template>
  <div>
    <Search/>
    <hr>
    <Listing/>
  </div>
</template>
<script>
import Search from '@/components/Search.vue';
import Listing from '@/components/Listing.vue';
export default {
  components: { Search, Listing },
};
</script>
