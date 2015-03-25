Rails.application.routes.draw do

  mount API::Root => '/'

  get '/doc', :to => 'doc#index'
end
