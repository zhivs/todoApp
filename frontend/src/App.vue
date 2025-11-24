<template>
  <div>
    <form @submit.prevent="addTodo">
      <input v-model="newTodo"
      type="text"
      placeholder="Введите задачу">

      <button type="submit">Добавить задачу</button>
    </form>

    <ul>
      <li
      v-for="todo in todos"
      :key="todo.id"
      >
      {{ todo.title }}
      </li>
    </ul>
  </div>
</template>

<script setup>

import {ref, onMounted} from 'vue'

import axios from 'axios';
//настроить путь до апи

const API_BASE = 'http://localhost:8000'

const newTodo = ref('')
const todos = ref([])

const loadTodos = async () => {
  
  const result = await axios.get(`${API_BASE}/todos`)
  todos.value = result.data
  console.log(result.data)
}

const addTodo = async () => {
    const result = await axios.post(`${API_BASE}/todos`, {
      title: newTodo.value,
      complited: false
    })

}

onMounted(loadTodos)
</script>