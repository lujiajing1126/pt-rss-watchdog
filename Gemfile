#source 'https://ruby.taobao.org'
source 'https://rubygems.org'

# Bundle edge Rails instead: gem 'rails', github: 'rails/rails'
gem 'rails', '4.2.1'
# Use SCSS for stylesheets
gem 'sass-rails', '~> 5.0'
# Use Uglifier as compressor for JavaScript assets
gem 'uglifier', '>= 1.3.0'
# Use CoffeeScript for .coffee assets and views
gem 'coffee-rails', '~> 4.1.0'
# See https://github.com/rails/execjs#readme for more supported runtimes
gem 'therubyracer', platforms: :ruby

# Use jquery as the JavaScript library
gem 'jquery-rails'
# Turbolinks makes following links in your web application faster. Read more: https://github.com/rails/turbolinks
gem 'turbolinks'
# Build JSON APIs with ease. Read more: https://github.com/rails/jbuilder
gem 'jbuilder', '~> 2.0'
# bundle exec rake doc:rails generates the API under doc/api.
gem 'sdoc', '~> 0.4.0', group: :doc
gem 'hashie-forbidden_attributes'

# Theme
gem 'bower-rails','~> 0.9.2'
gem 'less-rails'
gem 'twitter-bootstrap-rails'
gem 'nprogress-rails'

# Database
gem 'mongoid', github: 'mongoid/mongoid'

# Template Engine
gem 'slim'
gem 'kaminari'

# Notification
gem 'jpush', '~> 3.2.1'
gem 'sidekiq'

# API Layer
gem 'grape'
gem 'grape-entity'

# API Doc
gem 'grape-swagger'
gem 'swagger-ui_rails'
gem 'rack-cors'
gem 'kramdown'

# Use ActiveModel has_secure_password
# gem 'bcrypt', '~> 3.1.7'

# Use Unicorn as the app server
# gem 'unicorn'

# Use Capistrano for deployment
# gem 'capistrano-rails', group: :development

group :development, :test do
  # Server
  gem 'thin'
  # Call 'byebug' anywhere in the code to stop execution and get a debugger console
  gem 'byebug'

  # Debug Toolkit
  gem 'pry'
  gem 'pry-nav'

  # Access an IRB console on exception pages or by using <%= console %> in views
  gem 'web-console', '~> 2.0'

  # Spring speeds up development by keeping your application running in the background. Read more: https://github.com/rails/spring
  gem 'spring'

  # deploy
  gem 'capistrano','~> 3.4.0'
  gem 'capistrano-sidekiq'
  gem 'capistrano-rails'
  gem 'capistrano-rbenv'
  # gem 'capistrano-unicorn'
end

group :production do
  gem 'unicorn'
end

