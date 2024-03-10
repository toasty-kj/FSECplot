export interface UpdateHistory {
  // release: string
  release: 'major' | 'minor' | 'hotfix'
  author: string
  content: string
  date: string
  title: string
}

export interface UpdateHistoryByDate {
  date: string
  history: UpdateHistory[]
}
