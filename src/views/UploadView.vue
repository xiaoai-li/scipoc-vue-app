<template>
  <div class="upload">
      <div style="border: 1px solid gray; padding: 25px; border-radius: 5px;margin: 60px">
        <Upload />
      </div>
  </div>
</template>

<script>
// @ is an alias to /src
import Upload from '@/components/Upload.vue';

export default {
  name: 'UploadView',
  components: {
    Upload,
  },
};
</script>
