<template>
    <section>
        <div class="container">
            <div class="row">
                <div class="col-sm-12 col-lg-5 div m-3">
                    <h1 class="text-white">{{ images.title }}</h1>
                    <img width="100%" class="rounded my-3" :src="images.image" alt="">
                    <p class="text-white">{{ images.published }}</p>
                </div>
            </div>
        <!-- comment form -->
            <Comment :images="images.id" @reLoad="loadImages()"/>
            <div v-for="comment in images.comments_images" class="row">
                <div class="col-sm-12 col-lg-12 div m-3">
                    <h3 class="text-white">{{ comment.author }}</h3>
                    <p class="text-white">{{ comment.content }}</p>
                    <p class="text-white"> {{ comment.published }}</p>
                </div>
            </div>
        </div>
    </section>
</template>

<style scoped>

</style>

<script>
    import Comment from '../components/Comment'
    export default {
        name: 'SingleImages',
        props: ['id'],
        components: {Comment},
        data() {
            return {
                images: {}
            }
        },
        created() {
            this.loadImages()
        },
        methods: {
            async loadImages() {
                this.images = await fetch(
                    `${this.$store.getters.getServerUrl}/images/${this.id}/`
                ).then(response => response.json())
                console.log(this.images)
                console.log(this.id)
            }
        }
    }
</script>
