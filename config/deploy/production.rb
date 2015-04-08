set :stage, :production
set :rails_env, :production
set :rbenv_ruby, '2.1.5'

server 'l4.tokyo.hotshotxwl.tk:22222', {
    user: 'megrez',
    roles: %w{web app},
    ssh_options: {
        forward_agent: true,
    }
}

set :deploy_to, "/opt/ptrss/#{fetch(:stage)}"
set :branch, 'master'
set :sidekiq_pid ,File.join(shared_path, 'pids', 'sidekiq.pid')
set :sidekiq_config, File.join(current_path,'config','sidekiq.yml')


