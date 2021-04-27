<template>
  <div class="images">
      <section class="text-white">
          <div class="container">
          	<div class="row">
          		<div class="col-sm-12 col-lg-3 div m-3">
          			<a class="text-white btn btn-danger m-3" type="submit" @click="goToCreate()">Добавить фотку</a>
          		</div>
          	</div>
          	<div v-for="image in listImages.results" class="row">
          		<div class="col-sm-12 col-lg-5 div m-3">
          			<a @click="goTo(image.id)"><img width="100%"  class="rounded my-3" :src=" image.image "></a>
          		</div>
          	</div>
          </div>
      </section>
  </div>
</template>
<style scoped>
    /* .home {
        background: url("../assets/228.jpg");
    } */
</style>
<script>

export default {
  name: 'Images',
  data() {
    return {
        listImages: []
    }
  },
  components: {},
  created(){
      this.loadListImages()
  },
  methods: {
      async loadListImages() {
          this.listImages = await fetch(
              `${this.$store.getters.getServerUrl}/images/`
          ).then(response => response.json())
          console.log(this.listImages)
      },
      goTo(id) {
          this.$router.push({name: 'SingleImages', params: {id: id}})
      },
      goToCreate() {
          this.$router.push({name: 'CreateImages'})
      }
  }
}
</script>
