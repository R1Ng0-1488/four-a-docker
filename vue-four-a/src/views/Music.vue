<template>
  <div class="music">
      <section class="text-white">
          <div class="container">
          	<div v-for="music in listMusic.results" class="row">
          		<div class="col div m-3">
          			<h1 class="text-white border-danger"> {{ music.title }} </h1>
          			<p class="text-white"> {{ music.text }} </p>
          			<img v-if="music.image" class="rounded" width="300" height="300" :src="music.image">
          			<img v-else="" class="rounded" width="300" height="300" src="../assets/empty.png">
          			<p class="text-white font-italic"> {{ music.published }} </p>
          			<a :href="music.music"><img class="hovers m-2" width="50" height="50" src="../assets/vk-black.png"></a>

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
  name: 'Music',
  data() {
      return {
          listMusic: []
      }
  },
  components: {},
  created() {
      this.loadListMusic()
  },
  methods: {
      async loadListMusic() {
          this.listMusic = await fetch(
             `${this.$store.getters.getServerUrl}/music/`
         ).then(response => response.json())
         console.log(this.listMusic)
      }
  }
}
</script>
