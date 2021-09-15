<template>
  <div>
    <div>{{ title }}</div>
    <div v-text="title"></div>
    <div v-html="title"></div>
    <hr>
    <a v-bind:href="url" target="_blank">Vue 홈페이지</a><br>
    <a :href="url" target="_blank">Vue 홈페이지</a>
    <hr>
    <div>
      학습 레벨 : 
      <span v-if="level===0">초급</span>
      <span v-else-if="level===1">중급</span>
      <span v-else-if="level===2">고급</span>
      <span v-else-if="level===3">마스터</span>
      <span v-else>ㅇㅅㅇ</span>
    </div>
    <div>
      학습 레벨 : {{ level }}({{ levelTitle }})
    </div>
    <div>
      학습 레벨 : <span :class="levelClass">{{ level }}({{ levelTitle }})</span>
      <p :style="inlineCss">인라인 스타일링</p>
    </div>
    <div>
      <button v-on:click="levelUp">레벨 업</button>
      <button @click="levelDown">레벨 다운</button>
    </div>
    <h4>북마크</h4>
    <input v-model="bookmark_title">
    <input v-model="bookmark_url" @keydown.enter="addBookmark($event)">
    <button @click="addBookmark($event)">추가</button>
    <div>이름 : {{ bookmark_title }}</div>
    <div>url : {{ bookmark_url }}</div>
    <ul>
      <li v-for="(bookmark, ix) in bookmarks" :key="ix">
        <a :href="bookmark.url" target="_blank" @click.prevent>{{ bookmark.title }}</a>
        <button @click.meta="removeBookmark(ix)">삭제(윈도우키 + 클릭)</button>
      </li>
    </ul>
    <input type='checkbox' v-model="agreement"> 동의
    <div>{{ agreement ? '동의합니다' : '동의하지 않습니다.'}}</div>
    <input type='checkbox' v-model="favorites" value="사과"> 사과
    <input type='checkbox' v-model="favorites" value="배"> 배
    <input type='checkbox' v-model="favorites" value="오렌지"> 오렌지
    <div>{{ favorites }}</div>
    <select v-model="level">
      <option disabled value="">레벨 선택</option>
      <option v-for="l in levelOptions" :key="l.value" :value="l.value">{{ l.text }}</option>
    </select>
  </div>
</template>

<script>
export default {
  name: 'Example',
  data() {
    return {
      title: "<h3>Vue 연습</h3>",
      url: 'http://vuejs.org',
      bookmark_title: '',
      bookmark_url: '',
      bookmarks: [
        { title: 'Naver', url: 'https://naver.com' },
        { title: 'Daum', url: 'https://daum.net' },
        { title: 'Google', url: 'https://google.com' },
      ],
      level: 3,
      agreement: false, // 0도 되긴 됨
      favorites: [],
      levelOptions: [
        { text: '초급', value: 0 },
        { text: '중급', value: 1 },
        { text: '고급', value: 2 },
        { text: '마스터', value: 3 },
      ],
    }
  },
  computed: {
    levelTitle() {
      const titles = ['초급', '중급', '고급', '마스터']
      if (this.level >= 0 && this.level <= 3)
        return titles[this.level]
      return 'ㅇㅅㅇ'
    },
    levelClass() {
        return {
           beginner: this.level === 0,
           medium: this.level === 1,
           high: this.level === 2,
           master: this.level === 3,
           known: this.level < 0 || this.level > 3
        }
    },
    inlineCss() {
      return {
        color: 'red',
        fontSize: (16 + this.level*2) + 'px', 
        backgroundColor: 'lightgray',
      }
    }
  },
  methods: {
    levelUp() {
      if (this.level < 3) {
        ++this.level;
      }
    },
    levelDown() {
      if (this.level > 0) {
        --this.level;
      }
    },
    addBookmark(event) {
      console.log(event);
      // this.bookmarks.push({
      this.bookmarks.unshift({
        title: this.bookmark_title,
        url: this.bookmark_url
      });
      this.bookmark_title = '';
      this.bookmark_url = '';
    },
    removeBookmark(ix) {
      if (!confirm(`${this.bookmarks[ix].title}을(를) 삭제할까요?`))
        return;
      this.bookmarks.splice(ix, 1);
    },
  }
}
</script>

<style scoped>
.beginner {
    background-color: yellow
}
.medium {
    color: white;
    background-color: green
}
.high {
    color: white;
    background-color: blue
}
.master {
    color: white;
    background-color: navy
}
.unknown {
    background-color: red
}
</style>
