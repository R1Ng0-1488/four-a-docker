<template>
    <section>
        <div class="container">
            <div class="row">
                <div class="col-xs-12 col-lg-8 m-3 div">
                    <div class="row">
                        <div class="col-xs-12 col-md-6 col-lg-6 my-5">
            					<iframe v-if="news.video" width="100%" class="rounded"  :src="news.video" frameborder="0" allowfullscreen></iframe>

            					<img v-else="" width="100%" class="rounded"  :src="news.image">

                        </div>
                        <div class="col-xs-12 col-md-6 col-lg-6">
                            <h1 class="text-white border-danger">{{ news.title }}</h1>
        					<p class="text-white"> {{ news.text }} </p>
        					<p class="text-white text-right font-italic">{{ news.author }}</p>

        					<p class="text-right font-italic"><a class="text-danger" :href="news.source">Источник</a></p>

        					<p class="text-white text-right font-italic">{{ news.published }}</p>
                        </div>
                    </div>
                </div>
            </div>
            <!-- comment's form -->
            <Comment :news="news.id" @reLoad="loadNews()"/>
            <div v-for="comment in news.comments_news" class="row">

                <div class="col-xs-12 col-lg-8 m-3 div">
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
    import Comment from "../components/Comment"
    export default {
        name: 'SingleNews',
        props: ['id'],
        components: {Comment},
        data() {
            return {
                news: {}
            }
        },
        created() {
            this.loadNews()
        },
        methods: {
            async loadNews() {
                console.log(this.id)
                this.news = await fetch(
                    `${this.$store.getters.getServerUrl}/news/${this.id}`,
                    {
                        method: 'GET',
                        headers: {
                            'Content-Type': 'application/json',
                            'Authorization': 'Bearer 6mkCmDrH5ZtYIzQEAhcJoZB1S5bWlp'
                        }
                    }
                ).then(response => response.json())
                console.log(this.news)
            }
        }
    }
</script>
